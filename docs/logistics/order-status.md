# Get Order Status

**Endpoint:** <span class="api-method api-method--get">GET</span> <code>Base_URL/api/external/v1/get-order-status</code>

Retrieves the current status of an order.

#### Request Headers

Authorization: Bearer API-KEY

Accept: application/json

Content-Type: application/json

lang: en (optional, default: ar)

#### Query Parameters

order_id: 2127645

#### Response Examples

**Success Response (Status: 200)**

```json
{
  "order_status": "delivered",
  "order_timeline": [
    {
      "status": "new",
      "date": "2025-11-19 12:33:45"
    },
    {
      "status": "accepted",
      "date": "2025-11-19 12:33:46"
    },
    {
      "status": "arrived_to_store",
      "date": "2025-11-19 13:38:24"
    },
    {
      "status": "picked",
      "date": "2025-11-19 13:38:27"
    },
    {
      "status": "delivered",
      "date": "2025-11-19 13:39:13"
    },
    {
      "status": "returned",
      "date": "2025-11-19 13:49:13"
    }
  ]
}
```

#### Possible Status Values

- new

- accepted

- arrived_to_store

- picked

- cancelled

- delivered

- returned

**Error Response (Status: 400)**

```json
{
  "status": 400,
  "message": "Order not found"
}
```

**Authentication Error (Status: 401)**

```json
{
  "message": "Unauthenticated"
}
```
