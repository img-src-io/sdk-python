# Presets

## Overview

### Available Operations

* [list_presets](#list_presets) - List presets
* [create_preset](#create_preset) - Create preset
* [get_preset](#get_preset) - Get preset
* [update_preset](#update_preset) - Update preset
* [delete_preset](#delete_preset) - Delete preset

## list_presets

Returns all transformation presets for the authenticated user. Requires Pro plan.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPresets" method="get" path="/api/v1/settings/presets" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.presets.list_presets()

    assert res.list_presets_response is not None

    # Handle response
    print(res.list_presets_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListPresetsResponse1](../../models/listpresetsresponse1.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401, 403                  | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_preset

Creates a new transformation preset. Requires Pro plan.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPreset" method="post" path="/api/v1/settings/presets" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.presets.create_preset(request={
        "name": "thumbnail",
        "description": "200x200 thumbnail with cover fit",
        "params": {
            "w": 200,
            "h": 200,
            "fit": "cover",
            "format": "webp",
        },
    })

    assert res.preset is not None

    # Handle response
    print(res.preset)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreatePresetRequest](../../models/createpresetrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreatePresetResponse](../../models/createpresetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 400, 401, 403, 409        | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_preset

Returns a specific preset by ID. Requires Pro plan.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPreset" method="get" path="/api/v1/settings/presets/{id}" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.presets.get_preset(id="preset_abc123")

    assert res.preset is not None

    # Handle response
    print(res.preset)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | preset_abc123                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetPresetResponse](../../models/getpresetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401, 403, 404             | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## update_preset

Updates an existing preset. Requires Pro plan.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePreset" method="put" path="/api/v1/settings/presets/{id}" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.presets.update_preset(id="preset_abc123", name="card-image", description="Card thumbnail for product listings", params={
        "w": 400,
        "h": 300,
        "fit": "cover",
    })

    assert res.preset is not None

    # Handle response
    print(res.preset)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | preset_abc123                                                       |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | New preset name (1-50 characters)                                   | card-image                                                          |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | New description (max 200 characters, null to clear)                 | Card thumbnail for product listings                                 |
| `params`                                                            | Dict[str, *Nullable[Any]*]                                          | :heavy_minus_sign:                                                  | New transformation parameters                                       | {<br/>"w": 400,<br/>"h": 300,<br/>"fit": "cover"<br/>}              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UpdatePresetResponse](../../models/updatepresetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 400, 401, 403, 404, 409   | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_preset

Deletes a preset. Requires Pro plan.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletePreset" method="delete" path="/api/v1/settings/presets/{id}" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.presets.delete_preset(id="preset_abc123")

    assert res.delete_preset_response is not None

    # Handle response
    print(res.delete_preset_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | preset_abc123                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletePresetResponse1](../../models/deletepresetresponse1.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401, 403, 404             | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |