# Order Status Updates

### Update order

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/partner/order-update</code>

This API is used to update an order.

**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

#### *Payload*

- partner_order_id (string, required): Unique identifier for the partner order

- status (string, required): ex: D,C,A New status of the order (e.g., "delivered", "canceled", "accepted")

```json
{
  "partner_order_id": "{{sample_partner_order_id}}",
  "status": "C"
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
    "status": [
      "The selected status is invalid."
    ]
  }
}
```
