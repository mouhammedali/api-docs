# Logistics API

![](assets/logistics/media/image1.png)

**Staging URL**: https://integration.mrmandoob.info

**Production URL**: https://mrmandoob.com

**Note:** partners must send their ip's for both staging and production, so we can whitelist them.

### **1. Add Order** 

### **[POST] Base_URL/api/external/v1/add-order**

This API is used to add orders.

#### *Header*

```
Authorization: Bearer API-KEY
Accept:application/json
Content-Type:application/json
```

#### *Payload*

```json
{
"from_address": "الصحافة - الرياض",
"from_lat": "24.8150846",
"from_long": "46.6355146",
"from_name": "اسم المتجر",
"to_address": "RASB8105، 8105 وادي الريحان، 3546، الصحافة، الرياض 13321، السعودية",
"to_lat": "24.812710481322743",
"to_long": "46.63781248033047",
"customer": {
"phone": "523456722",
"name" : "mahmoud"
},
"merchant_order_id": "56776544" // optional
"vehicle_type": "1" // optional [1 => car , 3 => motorbike]
}
```

#### *Response*

#### Success response status: 200

```json
{
"message": "success",
"data": {
"order_id": 2127645,
"distance": "0.35", // note: by (KM)
}
}
```

Error response status: 401

```json
{
  "message": "unauthorized"
}
```

Error response status: 400

```json
{
  "message": "The given data was invalid."
}
```

V2

**Logistic API documentation**

MrMandoob.com

## **Environment URLs**

- **Staging URL:** https://integration.mrmandoob.info

- **Production URL:** https://mrmandoob.com

> **Important:** Partners must send their IP addresses for both staging and production environments to be whitelisted.

## **Authentication**

All API requests require authentication using a Bearer token in the Authorization header.

### **Common Headers**

Authorization: Bearer API-KEY

Accept: application/json

Content-Type: application/json

lang: en (optional, default: ar)

## **API Endpoints**

### **1. Cancel Order**

**Endpoint:** [POST] Base_URL/api/external/v1/cancel-order

Cancels an existing order. Only orders with specific statuses can be cancelled.

#### **Allowed Statuses for Cancellation**

- New

- Accepted

#### **Request Headers**

Authorization: Bearer API-KEY

Accept: application/json

Content-Type: application/json

lang: en (optional, default: ar)

#### **Request Payload**

```json
{
  "order_id": 2127645,
  "reason_of_cancel": "Client requested cancellation"
}
```

#### **Response Examples**

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

### **2. Return Order**

**Endpoint:** [POST] Base_URL/api/external/v1/return-order

Returns an order to the sender. Only orders with specific statuses can be returned.

#### **Allowed Statuses for Return**

- **Arrived To Store**

#### **Request Headers**

Authorization: Bearer API-KEY

Accept: application/json

Content-Type: application/json

lang: en (optional, default: ar)

#### **Request Payload**

```json
{
  "order_id": 2127645,
  "reason_of_cancel": "Client refused delivery"
}
```

#### **Response Examples**

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

### **3. Get Order Status**

**Endpoint:** [GET] Base_URL/api/external/v1/get-order-status

Retrieves the current status of an order.

#### **Request Headers**

Authorization: Bearer API-KEY

Accept: application/json

Content-Type: application/json

lang: en (optional, default: ar)

#### **Query Parameters**

order_id: 2127645

#### **Response Examples**

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

#### **Possible Status Values**

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

## **Error Handling**

### **Common HTTP Status Codes**

- **200:** Success

- **400:** Bad Request - Invalid parameters or operation not allowed

- **401:** Unauthenticated - Invalid or missing API key

### **Error Response Format**

All error responses follow a consistent format:

```json
{
  "status": 400,
  "message": "Error description"
}
```

# **Change Status Webhook**

**This webhook is used to notify the system when an order status is updated or order created (e.g., new, delivered, canceled, etc.).**

## **Endpoint Test URL**

**POST {{your webhook api url}}**

## **Endpoint Production URL**

**POST {{your webhook api url}}**

## **Description**

**When an order status changes, a webhook request will be sent to the above endpoint containing the order identifier, the new status, and the event metadata.**

## **Request Headers**

**Content-Type: application/json**

**Authorization: Bearer {your_webhook_key} *(optional)***

***Note: You can add an authorization key in the Bearer token to authorize the request.***

***Estimated Time of Arrival (eta)***

- ***eta (timestamp)***

- ***eta_minutes (number of minutes)***

## **Request Payload New Order Created**

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

## **Request Payload Update Order Status**

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

## **Request Payload Returned Order Status**

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

## **Request Payload Change Courier**

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

**Hint: Change Courier --- Webhook Sequence**

**When a courier is reassigned on an order, the system fires 3 webhooks in sequence**

**What happens internally**

1. Old courier is removed --- status set to new

The existing courier is unassigned. The order reverts to new status and an order_updated webhook is sent with courier fields as null.

2. New courier is assigned --- status set to accepted

The new courier is linked to the order and their details are populated. An order_updated webhook is sent with the new courier's information.

3. Courier change confirmation sent

A dedicated courier_changed webhook is sent containing the new courier details**.**

**4. Get Live Tracking For Orders**

  --------- ----------------------------------------------------------------
   **GET**  Base_URL/api/external/v1/live-tracking

  --------- ----------------------------------------------------------------

Retrieves the real-time GPS location of the driver assigned to a specific order.

**Request Headers**

```
Authorization: Bearer API-KEY
Accept: application/json
Content-Type: application/json
```

**Query Param**

```json
{
  "order_id": 216475
}
```

**Response Examples**

**Success Response --- Driver Assigned (Status: 200)**

```json
{
  "order_status": "accepted",
  "representative": {
    "longitude": "46.675120",
    "latitude": "24.747732"
  }
}
```

**Success Response --- No Driver Assigned (Status: 200)**

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
"message": "Rate limit exceeded. You can call this endpoint once every
3 minutes per order. Please try again in 161 second(s) (at 13:14:54).",
"retry_after": 161,
"retry_at": "13:14:54"
}
```

Note: This endpoint is rate-limited to 1 request per order every 3 minutes. Use retry_after (seconds) or retry_at (clock time) from the response to schedule your next request.

# **Driver Location Updated Webhook**

**This webhook is used to notify the logistic integration when a driver location is updated for an active order after pickup.**

## **Endpoint Test URL**

**POST {{your webhook api url}}**

## **Endpoint Production URL**

**POST {{your webhook api url}}**

## **Description**

**When the driver picks up the order, we will start sending the driver's location to the configured driver location webhook URL every 2 minutes until the order is delivered.**

## **Request Headers**

**Content-Type: application/json**

**Authorization: Bearer {your_webhook_key} *(optional)***

***Note: You can add an authorization key in the Bearer token to authorize the request.***

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

## **Request Payload Driver Location Updated**

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
