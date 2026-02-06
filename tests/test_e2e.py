"""End-to-end tests for the img-src Python SDK.

These tests run against a real API server and require:
  - IMGSRC_API_KEY: A valid img-src API key
  - IMGSRC_SERVER_URL: The API server URL (e.g. https://api-dev.img-src.io)
"""

import os
import struct
import time
import zlib

import pytest

from img_src import errors
from img_src.sdk import Imgsrc

API_KEY = os.environ.get("IMGSRC_API_KEY", "")
SERVER_URL = os.environ.get("IMGSRC_SERVER_URL", "")

skip_no_api_key = pytest.mark.skipif(
    not API_KEY or not SERVER_URL,
    reason="IMGSRC_API_KEY and IMGSRC_SERVER_URL must be set",
)


def make_png_bytes(width: int = 100, height: int = 100, color: tuple = (255, 0, 0)) -> bytes:
    """Generate a minimal valid PNG file using only stdlib (struct + zlib)."""
    signature = b"\x89PNG\r\n\x1a\n"

    # IHDR
    ihdr_data = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    ihdr = _make_chunk(b"IHDR", ihdr_data)

    # IDAT
    raw_rows = b""
    for _ in range(height):
        raw_rows += b"\x00"  # filter byte (None)
        for _ in range(width):
            raw_rows += bytes(color)
    compressed = zlib.compress(raw_rows)
    idat = _make_chunk(b"IDAT", compressed)

    # IEND
    iend = _make_chunk(b"IEND", b"")

    return signature + ihdr + idat + iend


def _make_chunk(chunk_type: bytes, data: bytes) -> bytes:
    chunk = chunk_type + data
    return struct.pack(">I", len(data)) + chunk + struct.pack(">I", zlib.crc32(chunk) & 0xFFFFFFFF)


def retry_until(fn, max_retries=5, delay=2.0):
    """Retry a callable with backoff until it returns a truthy value."""
    for i in range(max_retries):
        result = fn()
        if result:
            return result
        if i < max_retries - 1:
            time.sleep(delay * (i + 1))
    return None


@pytest.fixture(scope="module")
def sdk():
    s = Imgsrc(bearer_auth=API_KEY, server_url=SERVER_URL)
    yield s


@pytest.fixture(scope="module")
def uploaded_image(sdk):
    """Upload a test image and return its metadata. Cleaned up after all tests."""
    unique = int(time.time())
    png_data = make_png_bytes(color=(unique % 256, (unique >> 8) % 256, 0))

    res = sdk.images.upload_image(
        request={
            "file": {
                "file_name": "test-image.png",
                "content": png_data,
                "content_type": "image/png",
            },
            "target_path": f"__sdk_e2e_test/python/test-image-{unique}.png",
        }
    )
    assert res.upload_response is not None
    image_data = res.upload_response

    yield image_data

    # Cleanup: delete the uploaded image
    try:
        sdk.images.delete_image(id=image_data.id)
    except Exception:
        pass


@skip_no_api_key
class TestSettings:
    def test_get_settings(self, sdk):
        res = sdk.settings.get_settings()
        assert res.settings_response is not None
        settings = res.settings_response.settings
        assert settings.username is not None
        assert len(settings.username) > 0
        assert settings.default_quality > 0


@skip_no_api_key
class TestUsage:
    def test_get_usage(self, sdk):
        res = sdk.usage.get_usage()
        assert res.usage_response is not None
        usage = res.usage_response
        assert usage.plan is not None
        assert usage.total_images >= 0


@skip_no_api_key
class TestUpload:
    def test_upload_image(self, uploaded_image):
        assert uploaded_image.id is not None
        assert len(uploaded_image.id) > 0
        assert uploaded_image.url is not None
        assert uploaded_image.size > 0
        assert uploaded_image.format_ == "png"
        assert uploaded_image.visibility == "public"


@skip_no_api_key
class TestListImages:
    def test_list_images(self, sdk, uploaded_image):
        res = sdk.images.list_images(limit=50)
        assert res is not None
        assert res.image_list_response is not None
        assert res.image_list_response.total >= 0
        assert isinstance(res.image_list_response.images, list)


@skip_no_api_key
class TestSearchImages:
    def test_search_images(self, sdk, uploaded_image):
        def search():
            res = sdk.images.search_images(q="test-image")
            if res.search_response and res.search_response.results:
                for img in res.search_response.results:
                    if img.id == uploaded_image.id:
                        return img
            return None

        found = retry_until(search, max_retries=5, delay=2.0)
        assert found is not None, f"Uploaded image {uploaded_image.id} not found in search"


@skip_no_api_key
class TestGetImage:
    def test_get_image(self, sdk, uploaded_image):
        res = sdk.images.get_image(id=uploaded_image.id)
        assert res.metadata_response is not None
        meta = res.metadata_response
        assert meta.id == uploaded_image.id
        assert meta.visibility == "public"


@skip_no_api_key
class TestVisibility:
    def test_update_visibility(self, sdk, uploaded_image):
        try:
            # Change to private
            res = sdk.images.update_visibility(id=uploaded_image.id, visibility="private")
            assert res.update_visibility_response is not None
            assert res.update_visibility_response.visibility == "private"

            # Revert to public
            res = sdk.images.update_visibility(id=uploaded_image.id, visibility="public")
            assert res.update_visibility_response is not None
            assert res.update_visibility_response.visibility == "public"
        except errors.ErrorResponse as e:
            if e.raw_response.status_code == 403:
                pytest.skip("Private images require Pro plan")
            raise


@skip_no_api_key
class TestSignedURL:
    def test_create_signed_url(self, sdk, uploaded_image):
        try:
            res = sdk.images.create_signed_url(id=uploaded_image.id)
            assert res.signed_url_response is not None
            assert res.signed_url_response.signed_url is not None
        except errors.ErrorResponse as e:
            if e.raw_response.status_code == 403:
                pytest.skip("Signed URLs require Pro plan")
            raise


@skip_no_api_key
class TestPresets:
    def test_preset_crud(self, sdk):
        preset_name = f"sdk-e2e-test-{int(time.time())}"

        # List presets
        try:
            list_res = sdk.presets.list_presets()
            assert list_res.list_presets_response is not None
        except errors.ErrorResponse as e:
            if e.raw_response.status_code == 403:
                pytest.skip("Presets require Pro plan")
            raise

        # Create preset
        create_res = sdk.presets.create_preset(
            request={
                "name": preset_name,
                "params": {"w": 200, "h": 200, "fit": "cover"},
                "description": "E2E test preset",
            }
        )
        assert create_res.preset is not None
        preset_id = create_res.preset.id
        assert preset_id is not None

        try:
            # Get preset
            get_res = sdk.presets.get_preset(id=preset_id)
            assert get_res.preset is not None
            assert get_res.preset.name == preset_name

            # Update preset
            update_res = sdk.presets.update_preset(
                id=preset_id,
                name=preset_name,
                params={"w": 300, "h": 300, "fit": "contain"},
            )
            assert update_res.preset is not None
            assert update_res.preset.params["w"] == 300
        finally:
            # Delete preset
            del_res = sdk.presets.delete_preset(name=preset_name)
            assert del_res.delete_preset_response is not None


@skip_no_api_key
class TestDeleteImage:
    def test_delete_uploaded_image(self, sdk, uploaded_image):
        res = sdk.images.delete_image(id=uploaded_image.id)
        assert res.delete_response is not None


@skip_no_api_key
class TestSettingsUpdate:
    def test_update_and_revert_settings(self, sdk):
        # Get current settings
        current = sdk.settings.get_settings()
        assert current.settings_response is not None
        original_quality = current.settings_response.settings.default_quality

        # Change quality
        new_quality = 75 if original_quality != 75 else 85
        update_res = sdk.settings.update_settings(
            request={"default_quality": new_quality}
        )
        assert update_res.settings_update_response is not None

        # Verify the change
        verify = sdk.settings.get_settings()
        assert verify.settings_response is not None
        assert verify.settings_response.settings.default_quality == new_quality

        # Revert
        sdk.settings.update_settings(
            request={"default_quality": original_quality}
        )

        # Verify revert
        final = sdk.settings.get_settings()
        assert final.settings_response is not None
        assert final.settings_response.settings.default_quality == original_quality
