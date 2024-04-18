hi, this is an API-Shop with django-rest-framework 3.15.1

for use this project:

install python

create an virtual environment, then activate it

run these commands in project root : 

pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
pu manage.py runserver


for create a superuser(admin):
py manage.py createsuperuser
then fill the inputs




accounts:

  "auth/login/"
  methods : ["POST", ]
    body(required) : ["phone_number", "password"]
    response : a json includs "accsess" and "refresh" with values


  "auth/login/refresh/"
  methods : ["POST", ]
  body(required) : ["refresh-token", ]
  response : refresh token


  "auth/logout/"
  methods : ["POST", ]
  body : ["", ]
  header : Bearer {token}
  response : ""


  "auth/register/"
  methods : ["POST", ]
  body(required) : ["phone_number", "password"]
  response : ""


  "auth/forgot_password/"
  methods : ["POST", ]
  body(required) : ["phone_number", ]
  response : ""


  "auth/confirm/"
  methods : ["PUT", ]
  body : ["", ]
  session : ["otp", "user"]    *otp is a 4 digits one time password that sends by email or sms
  response : ""
  

  "auth/change_password/{user_id}/"
  methods : ["PUT", ]
  body : ["old_password", "password1", "password2"]
  response : ""

-----------------------------------------------

products:

  "products/"
  methods : ["GET", ]
    body : ["", ]
    response : a list of product variations 
    .
    products_variations [ 
      id,
      product_name, 
      product_model, 
      short_description, 
      features [key, value], 
      color [name, code],
      images.
      price, 
      discount(%), 
      price_with_discount, 
      quantity, 
      is_available, 
      created_at, 
        product[ id,
          name,
          complete_descriptions,
          is_available,
          created_at,
          brand [title, image],
          image [image, ]
          category [title, image]
          ]]
  
  "product-detail/{product_id}"
  methods : ["GET", ]
    body : ["", ]
    response : a single product variation for details
    products_variations [ 
      id,
      product_name, 
      product_model, 
      short_description, 
      features [key, value], 
      color [name, code],
      images.
      price, 
      discount(%), 
      price_with_discount, 
      quantity, 
      is_available, 
      created_at, 
        product[ id,
          name,
          complete_descriptions,
          is_available,
          created_at,
          brand [title, image],
          image [image, ]
          category [title, image]
        ]]

  "category/"
  methods : ["GET", ]
    body : ["", ]
    response : a list of category
    id,
    title,
    image,

-----------------------------------------------

carts:

  "cart/"
  methods : ["GET", ]
    body : ["", ]
    response : a list of carts
    .
    product_id,
    color,
    quantity,
    product [ 
      id,
      product_name, 
      product_model, 
      short_description, 
      features [key, value], 
      color [name, code],
      images.
      price, 
      discount(%), 
      price_with_discount, 
      quantity, 
      is_available, 
      created_at, 
        product[
          id,
          name,
          complete_descriptions,
          is_available,
          created_at,
          brand [title, image],
          image [image, ]
          category [title, image]
        ]]
      

  "cart/add-or-remove/"
  methods : ["POST", "DELETE"]
    body for POST : ["product_id", "quantity", "color"]
    body for DELETE : ["product_id", "color", ]
    response : a confirm message for DELETE or POST
    
-----------------------------------------------

dashboard:

  "dashboard/"
  methods : ["GET", "POST", "PUT"]
    body for POST : ["first_name", "last_name", "address", "state", "postalcode"]  
    body for PUT : optional
    response : a success message for POST or PUT

-----------------------------------------------

orders:

  "orders/"
  methods : ["GET", "POST", "DELETE"]
    body for POST : nothing (carts will be add to order automaticly)
    body for DELETE : ["code", ]
    response : a success message for POST or canceled message for DELETE

