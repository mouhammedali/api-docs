# Orders & Webhooks

### Cancel order

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/vendor/order-status-update</code>

This API is used to cancel an order.

#### Header

```
Authorization: Bearer {token}
```

#### Payload

```json
{
"channelLinkId": "66e959cf18a350f58e66a397",
"locationId": "66e959c418a350f58e66a35d9",
"channelOrderId":"256114",
"status":110 // 110 canceled , 120 failed // 20 prepared
"reason": "product not exist",
}
```

#### Response

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

### Vendor webhooks

### Place order

<span class="api-method api-method--post">POST</span> <code>vendor_Base_URL</code>

This API is used to place an order

#### Header

Expect authentication like this

```
Authorization: Bearer {token}
```

#### Payload

**Note:** The prices are multiplied by 100 as shown in the code (price * 100).

If the product have a variant

```json
{
"decimalDigits": 2,
"courier": "فيصل طاشكندي",
"channelLinkId": "674d67315963175ad854311d",
"locationLinkId": "67rf45rf4r8wec4c5r5rcr5",
"channelOrderId": "208158",
"channelOrderDisplayId": "208158",
"orderType": 2,
"deliveryIsAsap": true,
"orderIsAlreadyPaid": true,
"payment": {
"amount": 1125,
"type": 0
},
"items": [
{
"plu": "P-VA-ervO-2",
"name": "Product Variant Item",
"price": 1000,
"quantity": 1,
"subItems": [ //
{
"plu": "P-VA-Nfin-2-#V500#-",
"name": "Variant 2",
"price": 500,
"quantity": 1,
"subItems": [
{
"plu": "f5fv5r9wd5vgh",
"name": "modifier group",
"price": 0,
"quantity": 1,
}
]
}
]
}
],
"note": "",
"discounts": [
{
"type": "item_percent_off",
"provider": "channel",
"name": "coupon",
"channelDiscountCode": "XRLnc35x9f",
"value": 375,
"amount": 375
}
],
"discountTotal": -375
}
```

If product does not have a variant

```json
{
"decimalDigits": 2,
"courier": "فيصل طاشكندي",
"channelLinkId": "675be95a37dcdefee3b50e70",
"locationLinkId": "67rf45rf4r8wec4c5r5rcr5",
"channelOrderId": "208157",
"channelOrderDisplayId": "208157",
"orderType": 2,
"deliveryIsAsap": true,
"orderIsAlreadyPaid": true,
"payment": {
"amount": 4800,
"type": 0
},
"items": [
{
"plu": "sk-1113",
"name": "Little Double Beef Meal",
"price": 3000,//item price
"quantity": 14,
"subItems": [
{
"plu": "sk-1113",
"name": "addition item",
"price": 0,
"quantity": 14,
"subItems": []
}
]
},
{
"plu": "sk-1114",
"name": "Little Double Crispy Meal",
"price": 3000,
"quantity": 10,
"subItems": []
},
{
"plu": "sk-1115",
"name": "2 Little Double Beef Meal",
"price": 6000,
"quantity": 5,
"subItems": []
}
],
"note": "",
"discounts": [
{
"type": "item_percent_off",
"provider": "restaurant",
"name": "coupon",
"channelDiscountCode": "ATAvQyNChC",
"value": 10200,
"amount": 10200
},
{
"type": "unknown",
"provider": "restaurant",
"name": "item discount",
"channelDiscountCode": null,
"value": 21000, //item discount * quantity
"amount": 21000
},
{
"type": "unknown",
"provider": "restaurant",
"name": "item discount",
"channelDiscountCode": null,
"value": 15000,
"amount": 15000
},
{
"type": "unknown",
"provider": "restaurant",
"name": "item discount",
"channelDiscountCode": null,
"value": 15000,
"amount": 15000
}
],
"discountTotal": -61200
}
```

#### Expected Response

Status : 201

```
We expect status 201 created order successfully
```

Status : 400

```
Return validation errors
```

### Cancel order

<span class="api-method api-method--post">POST</span> <code>vendor_Base_URL</code>

This API is used to cancel an order from MrMandoob.

*Update: 02-02-2026*

We'll use this webhook to update all order statuses, starting with the Delivered status when the driver completes the order.

#### Header

Expect authentication like this

```
Authorization: Bearer {token}
```

#### Payload

```json
{
"channelOrderId": "1512154",
"channelOrderDisplayId": "1512154",
"cancellationReason": "Customer changed his mind",
"status": "CANCELLED", //CANCELLED or DELIVERED
"channelLinkId": 123
}
```

#### Expected Response

Status : 200

```
We expect status 200 order canceled successfully
```

Status : 400

```
Return validation errors
```

## Integration cycle

![](../assets/vendors/media/image5.png)

**Integration cycle**

![](../assets/vendors/media/image4.png)

**Order cycle**

![](../assets/vendors/media/image6.png)

**BigMenu**

> 🧩
>
> Big Menu Integration
>
> For supermarkets and pharmacies
>
> ![](../assets/vendors/media/image2.png)
