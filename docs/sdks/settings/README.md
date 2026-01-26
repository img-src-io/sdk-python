# Settings

## Overview

### Available Operations

* [get_settings](#get_settings) - Get user settings
* [update_settings](#update_settings) - Update user settings

## get_settings

Returns the authenticated user's settings

### Example Usage

<!-- UsageSnippet language="python" operationID="getSettings" method="get" path="/api/v1/settings" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.settings.get_settings()

    assert res.settings_response is not None

    # Handle response
    print(res.settings_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSettingsResponse](../../models/getsettingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401                       | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_settings

Updates the authenticated user's settings

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSettings" method="put" path="/api/v1/settings" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.settings.update_settings(request={
        "delivery_formats": [
            "webp",
            "avif",
            "jpeg",
        ],
        "default_quality": 80,
        "default_fit_mode": "contain",
        "default_max_width": 1920,
        "default_max_height": 1080,
        "theme": "dark",
        "language": "ko",
    })

    assert res.settings_update_response is not None

    # Handle response
    print(res.settings_update_response)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.UpdateSettingsRequest](../../models/updatesettingsrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.UpdateSettingsResponse](../../models/updatesettingsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 400, 401, 404             | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |