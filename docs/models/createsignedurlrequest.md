# CreateSignedURLRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `expires_in_seconds`                                           | *Optional[int]*                                                | :heavy_minus_sign:                                             | Expiration time in seconds (60-86400, default 3600)            | 3600                                                           |
| `transformation`                                               | [Optional[models.Transformation]](../models/transformation.md) | :heavy_minus_sign:                                             | Optional image transformation parameters                       |                                                                |