# Promotions & Inventory

###  **Add promotion [POST]** Base_URL/api/v1/productDiscount/add/{{partner_name}}

This API is used to add a discount on specific products.

**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.


**Payload**

```json
{
  "branch_id": "BRANCH001",
  "product_pid": "PROD123456789",
  "discount_price": 3599.0,
  "start_date": "2025-12-20",
  "end_date": "2025-12-31",
  "description": "iPhone 15 Pro New Year Sale"
}
```

**Response**

400

```json
{
  "status": "error",
  "message": "Failed to create promotion, Product or branch not found."
}
```

```json
{
  "status": "error",
  "message": "Failed to create promotion, Promotion already exists for product: 289375 in branch: 641241"
}
```

200

```json
{
  "status": "processed",
  "data": {
    "promotion_id": 430
  },
  "message": "Promotion processed successfully"
}
```

**update promotion**

###  **Update promotion [POST]** Base_URL/api/v1/productDiscount/update/{{partner_name}}

This API is used to update a discount date or description only.

**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.


**Payload**

```json
{
  "branch_id": "BRANCH001",
  "product_pid": "PROD123456789",
  "start_date": "2025-12-20",
  "end_date": "2025-12-31",
  "description": "iPhone 15 Pro New Year Sale"
}
```

**Response**

400

```json
{
  "status": "error",
  "message": "Failed to create promotion, Product or branch not found."
}
```

```json
{
  "status": "error",
  "message": "Failed to create promotion, Promotion already exists for product: 289375 in branch: 641241"
}
```

200

```
"status": "processed",
"data": {
"promotion_id": 430
},
"message": "Update Promotion processed successfully"
}
```

**delete promotion**

###  **Delete promotion[POST]** Base_URL/api/v1/productDiscount/delete/{{partner_name}}

This API is used to delete a discount.


**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.

**Payload**

```json
{
"branch_id": "BRANCH001",
"product_pid": "PROD123456789",
}
```

**Response**

400

```json
{
  "status": "error",
  "message": "Failed to delete promotion, Product or branch not found."
}
```

```json
{
  "status": "error",
  "message": "Failed to delete promotion, Promotion already exists for product: 289375 in branch: 641241"
}
```

200

```json
{
  "status": "success",
  "message": "Promotion deleted successfully."
}
```

**Product Inventory**

###  **Product Inventory[POST]** Base_URL/api/v1/productInventory/sync/{{partner_name}}

This API is used update qty and availability


**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.

**Payload**

```json
{
  "data": [
    {
      "branch_id": "location_id_641241",
      "product_id": "PROD1234567891",
      "status": "available",
      "qty": 0
    },
    {
      "branch_id": "67a9e7cbe8c87415d517b42f",
      "product_id": "PROD987654321",
      "status": "unavailable",
      "qty": 0
    },
    {
      "branch_id": "BRANCH002",
      "product_id": "PROD123456789",
      "status": "available",
      "qty": 25
    }
  ]
}
```

**Response**

400

```json
{
  "status": "error",
  "message": "Failed to process products , Branch or Product not found"
}
```

200

```json
{
  "status": "processed",
  "message": "Inventory processed successfully."
}
```

**Cancel order**
