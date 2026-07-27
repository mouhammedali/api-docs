# Products

### Add products

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/products/add/{{partner_name}}</code>

This API is used to add products for a big menu , max 1000 products.

**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.

This API is asynchronous and returns a "queued" status while it processes in the background.

- **callbackUrl :If the product addition fails, the system will send the result to the callback URL**

- **reference_id :Reference ID of the request, used to identify which request failed**

<!-- -->

- **products: Array wrapper for batch operations**

  - **id: Product identifier**

  - **en_name/ar_name: English and Arabic product names**

  - **en_description/ar_description: English and Arabic descriptions**

  - **price: Product price as decimal**

  - **is_active: Product status (true/false)**

  - **imageurls: Array of image URLs**

  - **subcategories: Array of category associations with parent references**

**Payload**

```json
{
  "callBackUrl": "yourCallbackUrl",
  "reference_id": "refercene id of request",
  "products": [
    {
      "id": "PROD123456789",
      "en_name": "iPhone 17 Pro",
      "ar_name": "آيفون 17 برو",
      "en_description": "Latest iPhone with advanced features",
      "ar_description": "أحدث آيفون مع ميزات متقدمة",
      "price": 2000.0,
      "is_active": true,
      "imageurls": [
        "https://cdn.example.com/catalog/small/iphone15pro1.jpg",
        "https://cdn.example.com/catalog/small/iphone15pro2.jpg"
      ],
      "parent_id": null,
      "subcategories": [
        {
          "id": "CAT123456789",
          "en_name": "Electronics",
          "ar_name": "إلكترونيات",
          "parentCategory": {
            "id": "CAT1234567893",
            "en_name": "Electronics",
            "ar_name": "إلكترونيات"
          }
        }
      ]
    },
    {
      "id": "PROD123456789",
      "en_name": "iPhone 17 Pro",
      "ar_name": "آيفون 17 برو",
      "en_description": "Latest iPhone with advanced features",
      "ar_description": "أحدث آيفون مع ميزات متقدمة",
      "price": 2000.0,
      "is_active": true,
      "imageurls": [
        "https://cdn.example.com/catalog/small/iphone15pro1.jpg",
        "https://cdn.example.com/catalog/small/iphone15pro2.jpg"
      ],
      "parent_id": null,
      "subcategories": [
        {
          "id": "CAT123456789",
          "en_name": "Electronics",
          "ar_name": "إلكترونيات",
          "parentCategory": null
        }
      ]
    },
    {
      "id": "PROD1234567891",
      "en_name": "iPhone 17 Pro",
      "ar_name": "آيفون 17 برو",
      "en_description": "Latest iPhone with advanced features",
      "ar_description": "أحدث آيفون مع ميزات متقدمة",
      "price": 2000.0,
      "is_active": true,
      "imageurls": [
        "https://cdn.example.com/catalog/small/iphone15pro1.jpg",
        "https://cdn.example.com/catalog/small/iphone15pro2.jpg"
      ],
      "parent_id": null,
      "subcategories": [
        {
          "id": "CAT123456789",
          "en_name": "Electronics",
          "ar_name": "إلكترونيات",
          "parentCategory": null
        }
      ]
    }
  ]
}
```

**Response**

400

```json
{
  "message": "The given data was invalid.",
  "errors": {
    "products": [
      "At least one product is required."
    ]
  }
}
```

200

```json
{
  "status": "queued",
  "message": "Products queued for processing."
}
```

**update products**

### Update products

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/products/update/{{partner_name}}</code>

This API is used to update products for a big menu , max 1000 products.

**Headers**

- **secretKey** -- your API key

- **apiKey** -- same value as secretKey

> ⚠️ Both headers must have **the same value** ($APIKEY) and be sent with **every request**, otherwise you'll get a **401 Unauthorized** error.

This API is asynchronous and returns a "queued" status while it processes in the background.

- **callbackUrl :If the product addition fails, the system will send the result to the callback URL**

- **reference_id :Reference ID of the request, used to identify which request failed**

<!-- -->

- **products: Array wrapper for batch operations**

  - **id: Product identifier**

  - **en_name/ar_name: English and Arabic product names**

  - **en_description/ar_description: English and Arabic descriptions**

  - **price: Product price as decimal**

  - **is_active: Product status (true/false)**

  - **imageurls: Array of image URLs**

  - **subcategories: Array of category associations with parent references**

**Payload**

```json
{
  "callBackUrl": "yourCallbackUrl",
  "reference_id": "refercene id of request",
  "products": [
    {
      "id": "PROD123456789",
      "en_name": "iPhone 17 Pro",
      "ar_name": "آيفون 17 برو",
      "en_description": "Latest iPhone with advanced features",
      "ar_description": "أحدث آيفون مع ميزات متقدمة",
      "price": 2000.0,
      "is_active": true,
      "imageurls": [
        "https://cdn.example.com/catalog/small/iphone15pro1.jpg",
        "https://cdn.example.com/catalog/small/iphone15pro2.jpg"
      ],
      "parent_id": null,
      "subcategories": [
        {
          "id": "CAT123456789",
          "en_name": "Electronics",
          "ar_name": "إلكترونيات",
          "parentCategory": null
        }
      ]
    },
    {
      "id": "PROD123456789",
      "en_name": "iPhone 17 Pro",
      "ar_name": "آيفون 17 برو",
      "en_description": "Latest iPhone with advanced features",
      "ar_description": "أحدث آيفون مع ميزات متقدمة",
      "price": 2000.0,
      "is_active": true,
      "imageurls": [
        "https://cdn.example.com/catalog/small/iphone15pro1.jpg",
        "https://cdn.example.com/catalog/small/iphone15pro2.jpg"
      ],
      "parent_id": null,
      "subcategories": [
        {
          "id": "CAT123456789",
          "en_name": "Electronics",
          "ar_name": "إلكترونيات",
          "parentCategory": null
        }
      ]
    },
    {
      "id": "PROD1234567891",
      "en_name": "iPhone 17 Pro",
      "ar_name": "آيفون 17 برو",
      "en_description": "Latest iPhone with advanced features",
      "ar_description": "أحدث آيفون مع ميزات متقدمة",
      "price": 2000.0,
      "is_active": true,
      "imageurls": [
        "https://cdn.example.com/catalog/small/iphone15pro1.jpg",
        "https://cdn.example.com/catalog/small/iphone15pro2.jpg"
      ],
      "parent_id": null,
      "subcategories": [
        {
          "id": "CAT123456789",
          "en_name": "Electronics",
          "ar_name": "إلكترونيات",
          "parentCategory": null
        }
      ]
    }
  ]
}
```

**Response**

400

```json
{
  "message": "The given data was invalid.",
  "errors": {
    "products": [
      "At least one product is required."
    ]
  }
}
```

200

```json
{
  "status": "queued",
  "message": "Products queued for processing."
}
```
