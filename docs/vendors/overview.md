# Overview & Authentication

### Create Token

<span class="api-method api-method--post">POST</span> <code>Auth_Base_URL/api/v1/create-token</code>

This API is used to create jwt tokens.

#### *Header*

```
Client-Secret:API KEY
Vendor : VENDOR_NAME
```

#### *Payload*

```json
{
  "scope": "vendors_scope",
  "grant_type": "client_credentials"
}
```

#### *Response*

#### status:200

```json
{
  "type": "Bearer",
  "token": "74a3bbcfca92f5e11289bb9876453b3c2fbc43ce7e8129c72e03a8cf57b28da6",
  "expires_at": 3599
}
```

Status 401 , 400

```json
{
  "message": "The given data was invalid."
}
```

### Get Days

<span class="api-method api-method--get">GET</span> <code>Base_URL/api/v1/vendor/days</code>

This API is used to retrieve the available days and their IDs.

#### *Payload*

This endpoint does not require a request payload.

#### *Response*

```json
[
{
"id": 1,
"name": "الأثنين",
"name_en": "Monday",
"code": "Mon"
},
{
"id": 2,
"name": "الثلاثاء",
"name_en": "Tuesday",
"code": "Tue"
},
{
"id": 3,
"name": "الأربعاء",
"name_en": "Wednesday",
"code": "Wed"
},
{
"id": 4,
"name": "الخميس",
"name_en": "Thursday",
"code": "Thu"
},
{
"id": 5,
"name": "الجمعة",
"name_en": "Friday",
"code": "Fri",
},
{
"id": 6,
"name": "السبت",
"name_en": "Saturday",
"code": "Sat",
},
{
"id": 7,
"name": "الأحد",
"name_en": "Sunday",
"code": "Sun",
}]
```

### Get allergens

<span class="api-method api-method--get">GET</span> <code>Base_URL/api/v1/vendor/allergens</code>

This API is used to retrieve all allergens.

#### *Payload*

This endpoint does not require a request payload.

#### *Response*

```json
[
{
"name": "Celery",
"allergenId": 100
},
{
"name": "Gluten",
"allergenId": 101
},
{
"name": "Crustaceans",
"allergenId": 102
},
{
"name": "Fish",
"allergenId": 103
},
{
"name": "Eggs",
"allergenId": 104
},
{
"name": "Lupin",
"allergenId": 105
},
{
"name": "Milk",
"allergenId": 106
},
{
"name": "Molluscs",
"allergenId": 107
},
{
"name": "Mustard",
"allergenId": 108
},
{
"name": "Nuts",
"allergenId": 109
},
{
"name": "Peanuts",
"allergenId": 110
},
{
"name": "Sesame",
"allergenId": 111
},
{
"name": "Soya",
"allergenId": 112
},
{
"name": "Sulphites",
"allergenId": 113
},
{
"name": "Almonds",
"allergenId": 114
},
{
"name": "Barley",
"allergenId": 115
},
{
"name": "Brazil Nuts",
"allergenId": 116
},
{
"name": "Cashew",
"allergenId": 117
},
{
"name": "Hazelnuts",
"allergenId": 118
},
{
"name": "Kamut",
"allergenId": 119
},
{
"name": "Macadamia",
"allergenId": 120
},
{
"name": "Oats",
"allergenId": 121
},
{
"name": "Pecan",
"allergenId": 122
},
{
"name": "Pistachios",
"allergenId": 123
},
{
"name": "Rye",
"allergenId": 124
},
{
"name": "Spelt",
"allergenId": 125
},
{
"name": "Walnuts",
"allergenId": 126
},
{
"name": "Wheat",
"allergenId": 127
},
{
"name": "Sugared Drink",
"allergenId": 128
},
{
"name": "Dairy",
"allergenId": 129
},
{
"name": "Lentils",
"allergenId": 130
},
{
"name": "Queensland Nuts",
"allergenId": 131
},
{
"name": "Shellfish",
"allergenId": 132
},
{
"name": "Treenuts",
"allergenId": 133
},
{
"name": "Sources Of Gluten",
"allergenId": 134
},
]
```
