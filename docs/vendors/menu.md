# Menu Management

### menu-update

<span class="api-method api-method--post">POST</span> <code>Base_URL/api/v1/vendor/menu-update/{location_id}</code>

This API is used to create or update location's menu.

**Note:** Price values are stored in halalas (1 SAR = 100 halalas). Multiply by 100 to convert to Saudi Riyals.

> **ملاحظة:** يتم تخزين الأسعار بالـ هللة (1 ريال = 100 هللة). اضرب القيمة في 100 للحصول على السعر بالريال السعودي.

#### Header

```
Authorization: Bearer {token}
```

#### Payload

```json
[
{
"reference_id": "refreance234",//reference_id to send in menu callback not required
"channelLinkId": "66e959cf18a350f58e66a397",//brand id which provided by Mrmandoob
"availabilities": [//locatiion's opening hours
{
"dayOfWeek": 1, // An integer value that indicates the day of the week for this availability (starting at 1 for Monday).
"endTime": "04:30",//A 24-hour HH:MM format notation of the start time of availability expressed in the local time of the location. must not exceed the midnight
"startTime": "00:00"//A 24-hour HH:MM format notation of the end time of availability expressed in the local time of the location,time slots on one day must not overlap
},
{
"dayOfWeek": 2,
"endTime": "23:30",
"startTime": "00:00"
},
{
"dayOfWeek": 3,
"endTime": "23:59",
"startTime": "00:00"
},
{
"dayOfWeek": 4,
"endTime": "23:00",
"startTime": "00:00"
},
{
"dayOfWeek": 5,
"endTime": "23:59",
"startTime": "00:00"
},
{
"dayOfWeek": 6,
"endTime": "23:59",
"startTime": "00:00"
},
{
"dayOfWeek": 7,
"endTime": "23:59",
"startTime": "00:00"
}
],
"categories": [
{
"_id": "6739b7fd9ee0bcefd4b61dbe",// required
"name": "Coffee", //english name
"nameTranslations": { // arabic name
"ar": "قهوة"
},
"description": "Coffee Description",//english description
"descriptionTranslations": {//arabic description
"ar": "القهوة الممتازه"
},
"imageUrl": ""//image url of the category ,
"availabilities": [],//category availabilities like location availabilities
"subProducts": [// products that exist under each category
"675187c29f7aecea91e7968e",
"681c9fe7ac16f73036318163",
"6739f55cd2825b13e6e57a79",
"673da0f3cae8ca6b92306a67",
"67ab0f48c68bf634ffba1c36"
]
}

],
"modifierGroups": {
"66e959cdc1e814b1174cf5ee": {
"_id": "66e959cdc1e814b1174cf5ee",//modifier id - required
"name": "Cooking instructions",// english name required
"nameTranslations": { // arabic name
"ar": "Cocinado"
},
"description": "Cocinado", // english description
"descriptionTranslations": { // arabic description
"ar": "كوكينادو"
},
"max": 1,//The maximum number of items the user must select
"min": 0,//The minimum number of items the user must select.
"plu": "",//This value should match the _id field
"productTags": [105], // array of allergens
"subProducts": [ // Modifier item IDs are listed under the modifiers key.
"66e959cdc1e814b1174cf5b0",
"66e959cdc1e814b1174cf5b2",
"66e959cdc1e814b1174cf5f0"
],
"snoozed": false //Indicates whether an item is snoozed at the point of a menu being published
}

},
"modifiers": {
"66e959cdc1e814b1174cf5b0": {
"_id": "66e959cdc1e814b1174cf5b0",
"name": "Rare",
"nameTranslations": {
"ar": "Poco hecho"
},
"description": "Poco hecho",
"descriptionTranslations": {
"ar": "Poco hecho"
},
"max": 0,
"min": 0,
"plu": "COOK-01",
"price": 0,
"productTags": [],
"subProducts": [],
"parentId": "66e959cdc1e814b1174cf5ee",
"snoozed": false
}
},
"products": {
"681c9fe7ac16f73036318166": {
"_id": "681c9fe7ac16f73036318166",
"name": "Min 3 max 3", //english name
"nameTranslations": {
"ar": "Min 3 max 3"//arabic name
},
"description": "Min 3 max 3",//english description
"descriptionTranslations": {//arabic description
"ar": ""
},
"imageUrl": "",
"isVariant": false,// Applicable to a product to indicate if it is a variant or not
"max": 3,//maximum number of items under a group to be purchased
"min": 3,//minimum number of items under a group to be purchased
"multiMax": 5,//max_quantity_per_order
"plu": ""//This value should match the _id field,
"price": 1000,
"subProducts": [//add the IDs of the modifier groups.,
"681c9fe7ac16f73036318167" //Modifier group IDs
],
"productTags": [105], // array of allergens
"sodium": 1,
"salt": 1,
},
"beverageInfo": {
"caffeine": 1,
},
 "snoozed": false
},
"681c9fe7ac16f73036318168": {
"_id": "681c9fe7ac16f73036318168",
"name": "Product Variant Item",
"description": "An Item Variant is a version of an Item with different ",
"descriptionTranslations": {},
"nameTranslations": {},
"imageUrl": "",
"isVariant": true,// Applicable to a product to indicate if it is a variant or not
"max": 0,//maximum number of items under a group to be purchased
"min": 0,//minimum number of items under a group to be purchased
"multiMax": 5,//max_quantity_per_order
"plu": ""//This value should match the _id field,
"price": 1000,
"productTags": [], // array of allergens
"subProducts": [//add the IDs of the modifier groups.,
"681c9fe7ac16f73036318167" //Modifier group IDs
],
"parentId": "673c4ef4898449e499cdb5d6",
"sodium": 1,
"salt": 1,
},
"beverageInfo": {
"caffeine": 1,
},
"snoozed": false //Indicates whether an item is snoozed at the point of a menu being published
}
}
}
]
```

#### Response

#### Status:200

```json
{
  "success": true
}
```

Status 401 , 400

```json
{
  "message": "The given data was invalid.",
  "errors": {
    "availabilities.1": [
      "Overlapping time slots found on day 1."
    ]
  }
}
```

```json
{
  "message": "JSON is not valid",
  "errors": null
}
```

Ex: [Complete Menu example](https://drive.google.com/file/d/16KQCnSq_b6eJWycBgh8d-kNs1w7d7odP/view?usp=sharing)(click)

```
Key
reference_id
channelLinkId
availabilities
availabilities[].dayOfWeek
availabilities[].startTime
availabilities[].endTime
categories
categories[]->_id
categories[].name
categories[].nameTranslations.ar
categories[].description
categories[].descriptionTranslations.ar
categories[].imageUrl
categories[].availabilities
categories[].subProducts
modifierGroups
modifierGroups.{id}._id
modifierGroups.{id}.name
modifierGroups.{id}.nameTranslations.ar
modifierGroups.{id}.description
modifierGroups.{id}.descriptionTranslations.ar
modifierGroups.{id}.max
modifierGroups.{id}.min
modifierGroups.{id}.plu
modifierGroups.{id}.productTags
modifierGroups.{id}.subProducts
modifierGroups.{id}.snoozed
modifiers
modifiers.{id}._id
modifiers.{id}.name
modifiers.{id}.nameTranslations.ar
modifiers.{id}.description
modifiers.{id}.descriptionTranslations.ar
modifiers.{id}.max
modifiers.{id}.min
modifiers.{id}.plu
modifiers.{id}.price
modifiers.{id}.productTags

modifiers.{id}.subProducts
modifiers.{id}.parentId
modifiers.{id}.snoozed
products
products.{id}._id
products.{id}.name
products.{id}.nameTranslations.ar
products.{id}.description
products.{id}.descriptionTranslations.ar
products.{id}.imageUrl
products.{id}.isVariant
products.{id}.max
products.{id}.min
products.{id}.multiMax
products.{id}.plu
products.{id}.price
products.{id}.productTags
products.{id}.subProducts
products.{id}.parentId
products.{id}.nutritionalInfo.sodium
products.{id}.nutritionalInfo.salt
products.{id}.beverageInfo.caffeine
products.{id}.snoozed
```
