# UpdatePresetRequest


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `name`                                              | *Optional[str]*                                     | :heavy_minus_sign:                                  | New preset name (1-50 characters)                   | card-image                                          |
| `description`                                       | *OptionalNullable[str]*                             | :heavy_minus_sign:                                  | New description (max 200 characters, null to clear) | Card thumbnail for product listings                 |
| `params`                                            | Dict[str, *Nullable[Any]*]                          | :heavy_minus_sign:                                  | New transformation parameters                       | {<br/>"w": 400,<br/>"h": 300,<br/>"fit": "cover"<br/>} |