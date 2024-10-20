MODELS FOLDER
The models folder contains all the models used for the product app. The various models are as follows:

A. products.py : This is a Django model for “Products” with fields for name, price, category, description, and image. It also includes static methods to retrieve products by ID, retrieve all products, and retrieve products by category ID.

B. category.py: This is a Django model for a “Category” that includes a name field with a maximum length of 50 characters. It also has a static method get_all_categories() to retrieve all the categories from the database. The __str__ method is defined to return the name of the category when it’s converted to a string.

C. customer.py: This is a Django model for a “Customer” with fields for name, phone, email, and password. It includes methods to register, retrieve customers by email, and check if a customer exists.

D. orders.py: This is a Django model for “Order” with fields for product, customer, quantity, price, address, phone, date, and status. It also includes methods to place an order and get orders by customer ID.


VIEWS FOLDER
 In views are the various views named home.py, login.py, signup.py, cart.py, checkout.py, orders.py  which takes a request and renders an HTML as a response. They create a home.html, login.html, signup.html, cart.html, checkout.html, orders.html in the templates. And map the views to the products\urls.py folder. 

 The below files show the views for each functionality of the site. 

A. home.py: This is a Django view for handling an online store. It includes methods for displaying the store’s index, adding or removing items from the cart, and rendering the store’s product listings. The view also uses Django sessions to manage the user’s shopping cart.