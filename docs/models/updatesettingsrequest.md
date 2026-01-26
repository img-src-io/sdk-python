# UpdateSettingsRequest


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `delivery_formats`                     | List[*str*]                            | :heavy_minus_sign:                     | Preferred delivery formats (ordered)   | [<br/>"webp",<br/>"avif",<br/>"jpeg"<br/>] |
| `default_quality`                      | *Optional[int]*                        | :heavy_minus_sign:                     | Default image quality (1-100)          | 80                                     |
| `default_fit_mode`                     | *Optional[str]*                        | :heavy_minus_sign:                     | Default fit mode                       | contain                                |
| `default_max_width`                    | *OptionalNullable[int]*                | :heavy_minus_sign:                     | Default maximum width (null to clear)  | 1920                                   |
| `default_max_height`                   | *OptionalNullable[int]*                | :heavy_minus_sign:                     | Default maximum height (null to clear) | 1080                                   |
| `theme`                                | *Optional[str]*                        | :heavy_minus_sign:                     | UI theme                               | dark                                   |
| `language`                             | *Optional[str]*                        | :heavy_minus_sign:                     | UI language                            | ko                                     |