# Images

## Overview

### Available Operations

* [upload_image](#upload_image) - Upload image
* [list_images](#list_images) - List images
* [search_images](#search_images) - Search images
* [get_image](#get_image) - Get image metadata
* [delete_image](#delete_image) - Delete image
* [create_signed_url](#create_signed_url) - Create signed URL
* [delete_image_path](#delete_image_path) - Delete image path

## upload_image

Upload a new image. Supports multipart/form-data with 'file' field.

### Example Usage

<!-- UsageSnippet language="python" operationID="uploadImage" method="post" path="/api/v1/images" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.images.upload_image(request={
        "target_path": "blog/2024",
    })

    assert res.upload_response is not None

    # Handle response
    print(res.upload_response)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.UploadImageRequestBody](../../models/uploadimagerequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.UploadImageResponse](../../models/uploadimageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 400, 401, 409, 413        | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_images

List user's images with pagination and optional path filtering

### Example Usage

<!-- UsageSnippet language="python" operationID="listImages" method="get" path="/api/v1/images" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.images.list_images(limit=50, offset=0, path="blog/2024")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListImagesResponse](../../models/listimagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401                       | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## search_images

Search images by filename

### Example Usage

<!-- UsageSnippet language="python" operationID="searchImages" method="get" path="/api/v1/images/search" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.images.search_images(q="vacation", limit=20)

    assert res.search_response is not None

    # Handle response
    print(res.search_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `q`                                                                 | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchImagesResponse](../../models/searchimagesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 400, 401                  | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_image

Get metadata for a specific image

### Example Usage

<!-- UsageSnippet language="python" operationID="getImage" method="get" path="/api/v1/images/{id}" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.images.get_image(id="<id>")

    assert res.metadata_response is not None

    # Handle response
    print(res.metadata_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetImageResponse](../../models/getimageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401, 404                  | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_image

Delete an image and all its paths

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteImage" method="delete" path="/api/v1/images/{id}" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.images.delete_image(id="abcdef1234567890")

    assert res.delete_response is not None

    # Handle response
    print(res.delete_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteImageResponse](../../models/deleteimageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401, 404                  | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_signed_url

Create a time-limited signed URL for an image (Pro plan only)

### Example Usage

<!-- UsageSnippet language="python" operationID="createSignedUrl" method="post" path="/api/v1/images/{id}/signed-url" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.images.create_signed_url(id="abcdef1234567890", expires_in_seconds=3600)

    assert res.signed_url_response is not None

    # Handle response
    print(res.signed_url_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `expires_in_seconds`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Expiration time in seconds (60-86400, default 3600)                 | 3600                                                                |
| `transformation`                                                    | [Optional[models.Transformation]](../../models/transformation.md)   | :heavy_minus_sign:                                                  | Optional image transformation parameters                            |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CreateSignedURLResponse](../../models/createsignedurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401, 403, 404             | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_image_path

Delete a specific path from an image. If this is the last path, the image is deleted.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteImagePath" method="delete" path="/api/v1/images/path/{username}/{filepath}" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.images.delete_image_path(username="johndoe", filepath="blog/2024/photo.webp")

    assert res.path_delete_response is not None

    # Handle response
    print(res.path_delete_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `username`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `filepath`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteImagePathResponse](../../models/deleteimagepathresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401, 403, 404             | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |