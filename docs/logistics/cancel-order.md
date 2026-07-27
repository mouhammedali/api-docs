# Cancel Order

### Cancel Order

**Endpoint:** <span class="api-method api-method--post">POST</span> <code>Base_URL/api/external/v1/cancel-order</code>

Cancels an existing order. Only orders with specific statuses can be cancelled.

#### Allowed Statuses for Cancellation

- New

- Accepted

#### Request Headers

Authorization: Bearer API-KEY

Accept: application/json

Content-Type: application/json

lang: en (optional, default: ar)

#### Request Payload

```json
{
  "order_id": 2127645,
  "reason_of_cancel": "Client requested cancellation"
}
```

#### Response Examples

**Success Response (Status: 200)**

```json
{
  "status": 200,
  "message": "Your order was cancelled successfully"
}
```

**Error Response (Status: 400)**

```json
{
  "status": 400,
  "message": "You cannot cancel order ."
}
```

**Authentication Error (Status: 401)**

```json
{
  "message": "Unauthenticated"
}
```
