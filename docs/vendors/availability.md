# Availability & Timing

### busy-mode

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/vendor/busy-mode</code>

This API is used to make a location in busy mode to stop receiving orders.

#### *Header*

```
Authorization: Bearer {token}
```

#### *Payload*

```json
{
"status": "PAUSED", // PAUSED or ONLINE
"channelLinkId": "66e959cf18a350f58e66a397",
"locationId": "66e959c418a350f58e66a359",
"accountId": "1" // required with 1
}
```

#### *Response*

Status : 200

```json
{
  "message": "Status updated"
}
```

Status 400

```json
{
  "message": "Validation failed",
  "errors": {
    "status": [
      "The selected status is invalid."
    ]
  }
}
```

### Snooze Unsnooze Product or modifier item

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/vendor/snoozeUnsnooze</code>

This API is used to make a product or a modifier item Snooze or Unsnooze.

#### *Header*

```
Authorization: Bearer {token}
```

#### *Payload*

```json
{
  "accountId": "",
  "locationId": "5ewff4ed48ededeed",
  "channelLinkId": "5c4f5c4f5c4f5c45f",
  "operations": [
    {
      "action": "snooze",
      "data": {
        "items": [
          {
            "plu": "qws45w4s5qw4d5"
          },
          {
            "plu": "ds45cr8cr54r4c5"
          }
        ]
      }
    },
    {
      "action": "unsnooze",
      "data": {
        "items": [
          {
            "plu": "fv4f5v4f8fv"
          },
          {
            "plu": "5e48asx4e8xe5ef"
          }
        ]
      }
    }
  ]
}
```

#### *Response*

Status : 200

```json
[]
```

Status : 400

```json
{
  "message": "Validation failed",
  "errors": {
    "operations.0.data.items.1.plu": [
      "The operations.0.data.items.1.plu field is required."
    ]
  }
}
```

### Update Prep Time

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/vendor/updatePrepTime</code>

This API is used to send order preparation time

#### *Header*

```
Authorization: Bearer {token}
```

#### *Payload*

```json
{
  "orderId": "",
  "locationId": "5ewff4ed48ededeed",
  "channelLinkId": "5c4f5c4f5c4f5c45f",
  "pickupTime": "2025-05-01 12:25:30"
}
```

#### *Response*

Status : 200

```json
[]
```

Status : 400

```json
[]
```
