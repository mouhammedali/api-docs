# Categories

### Add Category

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/categories/add/{{partner_name}}</code>

This API is used to create a single category for a big menu.

**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.

**This API is synchronous and responds instantly.**

- **en_name: English category name**

- **ar_name: Arabic category name**

- **category_id: Unique category identifier**

- **parent_id: null for parent categories**

- **image_url: Category image URL**

- **active: Category status (true/false)**

**Payload**

```json
{
  "en_name": "laptops",
  "ar_name": "لابتوبات",
  "category_id": "CAT1234567893",
  "parent_id": "",
  "image_url": "https://cdn.example.com/catalog/small/electronics.jpg",
  "active": true
}
```

Response

404

```json
{
  "status": "error",
  "message": "Merchant main menu not found."
}
```

200

```json
{
  "status": "processed",
  "message": "Category processed successfully.",
  "data": {
    "success": true,
    "local_id": 15366,
    "external_id": "CAT1234567893",
    "menu_id": "0"
  }
}
```

**edit category**

### Update Category

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/categories/update/{{partner_name}}</code>

This API is used to update a single category for a big menu.

**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.

**This API is synchronous and responds instantly.**

- **en_name: English category name**

- **ar_name: Arabic category name**

- **category_id: Unique category identifier**

- **parent_id: null for parent categories**

- **image_url: Category image URL**

- **active: Category status (true/false)**

**Payload**

```json
{
  "en_name": "laptops",
  "ar_name": "لابتوبات",
  "category_id": "CAT1234567893",
  "parent_id": "",
  "image_url": "https://cdn.example.com/catalog/small/electronics.jpg",
  "active": true
}
```

Response

404

```json
{
  "status": "error",
  "message": "Merchant main menu not found."
}
```

200

```json
{
  "status": "processed",
  "message": "Category processed successfully.",
  "data": {
    "success": true,
    "local_id": 15366,
    "external_id": "CAT1234567893",
    "menu_id": "0"
  }
}
```
