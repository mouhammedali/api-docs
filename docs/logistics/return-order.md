# Return Order

### Return Order

**Endpoint:** <span class="api-method api-method--post">POST</span> <code>Base_URL/api/external/v1/return-order</code>

Returns an order to the sender. Only orders with specific statuses can be returned.

#### Allowed Statuses for Return

- **Arrived To Store**

#### Request Headers

Authorization: Bearer API-KEY

Accept: application/json

Content-Type: application/json

lang: en (optional, default: ar)

#### Request Payload

```json
{
  "order_id": 2127645,
  "reason_of_cancel": "Client refused delivery"
}
```

#### Response Examples

**Success Response (Status: 200)**

```json
{
  "status": 200,
  "message": "Order returned successfully"
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
