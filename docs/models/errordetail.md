# ErrorDetail


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `code`                                                       | *str*                                                        | :heavy_check_mark:                                           | Error code (e.g., NOT_FOUND, UNAUTHORIZED, VALIDATION_ERROR) | NOT_FOUND                                                    |
| `message`                                                    | *str*                                                        | :heavy_check_mark:                                           | Human-readable error message                                 | The requested resource was not found                         |
| `status`                                                     | *int*                                                        | :heavy_check_mark:                                           | HTTP status code                                             | 404                                                          |
| `path`                                                       | *Optional[str]*                                              | :heavy_minus_sign:                                           | Request path (optional)                                      | /api/v1/images/nonexistent                                   |