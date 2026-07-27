# Driver Location Webhook

This webhook is used to notify the logistic integration when a driver location is updated for an active order after pickup.

## Endpoint Test URL

`POST {{your webhook api url}}`

## Endpoint Production URL

`POST {{your webhook api url}}`

## Description

When the driver picks up the order, we will start sending the driver's location to the configured driver location webhook URL every 2 minutes until the order is delivered.

## Request Headers

```
Content-Type: application/json
Authorization: Bearer {your_webhook_key} (optional)
```

**Note:** You can add an authorization key in the Bearer token to authorize the request.

- **event: always driver_location_updated**

- **event_time: webhook send time**

- **order_id: Mr. Mandoob order ID**

- **merchant_order_id: merchant/external order ID, if configured**

- **courier_id: driver ID**

- **courier_name: driver name**

- **courier_lat: latest driver latitude**

- **courier_long: latest driver longitude**

- **courier_phone: driver phone number with country code**

- **location_updated_at: time when the driver location was last updated in Mr. Mandoob system**

## Request Payload Driver Location Updated

```json
{
  "event": "driver_location_updated",
  "event_time": "2026-05-12 12:20:44",
  "order_id": 212853,
  "merchant_order_id": "98765",
  "courier_id": 1024,
  "courier_name": "Driver Name",
  "courier_lat": 24.697347,
  "courier_long": 46.681999,
  "courier_phone": "966555555555"
}
```
