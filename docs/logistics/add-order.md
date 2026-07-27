# Add Order

![](../assets/logistics/media/image1.png)

**Staging URL**: https://integration.mrmandoob.info

**Production URL**: https://mrmandoob.com

**Note:** partners must send their ip's for both staging and production, so we can whitelist them.

### Add Order

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/external/v1/add-order</code>

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
