# CurrentPeriod


## Fields

| Field                               | Type                                | Required                            | Description                         | Example                             |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `period`                            | *str*                               | :heavy_check_mark:                  | Period identifier (YYYY-MM format)  | 2025-01                             |
| `period_start`                      | *int*                               | :heavy_check_mark:                  | Unix timestamp of period start      | 1735689600                          |
| `period_end`                        | *int*                               | :heavy_check_mark:                  | Unix timestamp of period end        | 1738368000                          |
| `uploads`                           | *int*                               | :heavy_check_mark:                  | Uploads this period                 | 42                                  |
| `bandwidth_bytes`                   | *int*                               | :heavy_check_mark:                  | Bandwidth used this period in bytes | 1073741824                          |
| `api_requests`                      | *int*                               | :heavy_check_mark:                  | API requests this period            | 5000                                |
| `transformations`                   | *int*                               | :heavy_check_mark:                  | Image transformations this period   | 500                                 |