# CreatePresetRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `name`                                                   | *str*                                                    | :heavy_check_mark:                                       | Preset name (1-50 characters)                            | thumbnail                                                |
| `description`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Optional description (max 200 characters)                | 200x200 thumbnail with cover fit                         |
| `params`                                                 | Dict[str, *Nullable[Any]*]                               | :heavy_check_mark:                                       | Transformation parameters                                | {<br/>"w": 200,<br/>"h": 200,<br/>"fit": "cover",<br/>"format": "webp"<br/>} |