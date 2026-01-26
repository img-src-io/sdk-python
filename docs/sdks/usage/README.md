# Usage

## Overview

### Available Operations

* [get_usage](#get_usage) - Get usage statistics

## get_usage

Returns usage statistics for the authenticated user

### Example Usage

<!-- UsageSnippet language="python" operationID="getUsage" method="get" path="/api/v1/usage" -->
```python
from img_src import Imgsrc


with Imgsrc(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as imgsrc:

    res = imgsrc.usage.get_usage()

    assert res.usage_response is not None

    # Handle response
    print(res.usage_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetUsageResponse](../../models/getusageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.ErrorResponse      | 401                       | application/json          |
| errors.ErrorResponse      | 500                       | application/json          |
| errors.ImgsrcDefaultError | 4XX, 5XX                  | \*/\*                     |