# Change Status Webhook

This webhook is used to notify the system when an order status is updated or order created (e.g., new, delivered, canceled, etc.).

## Endpoint Test URL

`POST {{your webhook api url}}`

## Endpoint Production URL

`POST {{your webhook api url}}`

## Description

When an order status changes, a webhook request will be sent to the above endpoint containing the order identifier, the new status, and the event metadata.

## Request Headers

```
Content-Type: application/json
Authorization: Bearer {your_webhook_key} (optional)
```

**Note:** You can add an authorization key in the Bearer token to authorize the request.

**Estimated Time of Arrival (eta)**

- eta (timestamp)

- eta_minutes (number of minutes)

## Request Payload New Order Created

```json
{
  "event": "order_created",
  "event_time": "2025-12-23 12:20:44",
  "order_id": 212853,
  "order_status": "new",
  "courier_name": null,
  "courier_lat": null,
  "courier_long": null,
  "courier_phone": null,
  "eta": null,
  "eta_minutes": null,
  "order": {
    "merchant_order_id": "98765",
    "from_address": "Test Address",
    "from_lat": 24.697347,
    "from_long": 46.681999,
    "from_name": "Warehouse A",
    "to_address": "Test Address",
    "to_lat": 24.7135,
    "to_long": 46.6752,
    "customer": {
      "phone": "966555555555",
      "name": "Customer Name"
    }
  }
}
```

## Request Payload Update Order Status

```json
{
"event": "order_updated",
"event_time": "2025-12-23 12:20:44",
"order_id": 212853,
"order_status": "delivered",
"courier_name": "Courier Name",
"courier_lat": 24.697347,
"courier_long": 46.681999,
"courier_phone": "966555555555",
"eta": "2026-02-09 14:10:58",
"eta_minutes": "57",
}
```

## Request Payload Returned Order Status

```json
{
"event": "order_returned",
"event_time": "2025-12-23 12:20:44",
"order_id": 212853,
"order_status": "returned",
"courier_name": "Courier Name",
"courier_lat": 24.697347,
"courier_long": 46.681999,
"courier_phone": "966555555555",
"eta": "2026-02-09 14:10:58",
"eta_minutes": "57",
}
```

## Request Payload Change Courier

```json
{
"event": "courier_changed",
"event_time": "2025-12-23 12:20:44",
"order_id": 212853,
"order_status": "accepted",
"courier_name": "Courier Name",
"courier_lat": 24.697347,
"courier_long": 46.681999,
"courier_phone": "966555555555",
"eta": "2026-02-09 14:10:58",
"eta_minutes": "57",
}
```

#### Change Courier Webhook Sequence

When a courier is reassigned on an order, the system fires 3 webhooks in sequence.

**What happens internally:**

1. Old courier is removed — status set to new. The existing courier is unassigned. The order reverts to new status and an order_updated webhook is sent with courier fields as null.

2. New courier is assigned — status set to accepted. The new courier is linked to the order and their details are populated. An order_updated webhook is sent with the new courier's information.

3. Courier change confirmation sent. A dedicated courier_changed webhook is sent containing the new courier details.

### Get Live Tracking For Orders

<span class="api-method api-method--get">GET</span> <code>Base_URL/api/external/v1/live-tracking</code>

Retrieves the real-time GPS location of the driver assigned to a specific order.

#### Request Headers

```
Authorization: Bearer API-KEY
Accept: application/json
Content-Type: application/json
```

#### Query Parameters

```json
{
  "order_id": 216475
}
```

#### Response Examples

**Success Response — Driver Assigned (Status: 200)**

```json
{
  "order_status": "accepted",
  "representative": {
    "longitude": "46.675120",
    "latitude": "24.747732"
  }
}
```

**Success Response — No Driver Assigned (Status: 200)**

```json
{
  "order_status": "new",
  "representative": null,
  "message": "No driver has been assigned to this order yet."
}
```

**Rate Limit Exceeded (Status: 429)**

```json
{
  "message": "Rate limit exceeded. You can call this endpoint once every 3 minutes per order. Please try again in 161 second(s) (at 13:14:54).",
  "retry_after": 161,
  "retry_at": "13:14:54"
}
```

**Note:** This endpoint is rate-limited to 1 request per order every 3 minutes. Use retry_after (seconds) or retry_at (clock time) from the response to schedule your next request.
