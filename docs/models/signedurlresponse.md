# SignedURLResponse


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `signed_url`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Time-limited signed URL                                             | https://cdn.img-src.io/john/photo.webp?token=xxx&expires=1704153600 |
| `expires_at`                                                        | *int*                                                               | :heavy_check_mark:                                                  | Expiration timestamp (Unix epoch)                                   | 1704153600                                                          |
| `expires_in_seconds`                                                | *int*                                                               | :heavy_check_mark:                                                  | Seconds until expiration                                            | 3600                                                                |