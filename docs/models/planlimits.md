# PlanLimits


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `max_uploads_per_month`                                    | *Nullable[int]*                                            | :heavy_check_mark:                                         | Maximum uploads per month (null = unlimited)               | 1000                                                       |
| `max_storage_bytes`                                        | *Nullable[int]*                                            | :heavy_check_mark:                                         | Maximum storage in bytes (null = unlimited)                | 5368709120                                                 |
| `max_bandwidth_per_month`                                  | *Nullable[int]*                                            | :heavy_check_mark:                                         | Maximum bandwidth per month in bytes (null = unlimited)    | 10737418240                                                |
| `max_api_requests_per_month`                               | *Nullable[int]*                                            | :heavy_check_mark:                                         | Maximum API requests per month (null = unlimited)          | 100000                                                     |
| `max_transformations_per_month`                            | *Nullable[int]*                                            | :heavy_check_mark:                                         | Maximum image transformations per month (null = unlimited) | 10000                                                      |