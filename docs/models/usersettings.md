# UserSettings


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `id`                                    | *str*                                   | :heavy_check_mark:                      | Clerk user ID                           | user_abc123                             |
| `username`                              | *str*                                   | :heavy_check_mark:                      | Username                                | johndoe                                 |
| `email`                                 | *Optional[str]*                         | :heavy_minus_sign:                      | Email address                           | john@example.com                        |
| `delivery_formats`                      | List[*str*]                             | :heavy_check_mark:                      | Preferred delivery formats (ordered)    | [<br/>"webp",<br/>"avif",<br/>"jpeg"<br/>] |
| `default_quality`                       | *int*                                   | :heavy_check_mark:                      | Default image quality (1-100)           | 80                                      |
| `default_fit_mode`                      | *str*                                   | :heavy_check_mark:                      | Default fit mode                        | contain                                 |
| `default_max_width`                     | *Optional[int]*                         | :heavy_minus_sign:                      | Default maximum width                   | 1920                                    |
| `default_max_height`                    | *Optional[int]*                         | :heavy_minus_sign:                      | Default maximum height                  | 1080                                    |
| `theme`                                 | *str*                                   | :heavy_check_mark:                      | UI theme                                | light                                   |
| `language`                              | *str*                                   | :heavy_check_mark:                      | UI language                             | en                                      |
| `created_at`                            | *int*                                   | :heavy_check_mark:                      | Account creation timestamp (Unix epoch) | 1704067200                              |
| `updated_at`                            | *int*                                   | :heavy_check_mark:                      | Last update timestamp (Unix epoch)      | 1704067200                              |
| `total_uploads`                         | *int*                                   | :heavy_check_mark:                      | Total number of uploads                 | 150                                     |
| `storage_used_bytes`                    | *int*                                   | :heavy_check_mark:                      | Total storage used in bytes             | 104857600                               |