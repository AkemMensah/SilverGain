
---

# SilverGain E-Commerce App Documentation

## 1. **Overview**
SilverGain is a dynamic and user-friendly e-commerce platform designed to connect buyers and sellers globally. It facilitates the seamless buying and selling of both new and used products while catering to individuals, small businesses, and online retailers.

**Tagline**: "Buy". "Sell". "Connect."

### **Target Audience**
- Individuals looking to buy or sell new/used products
- Small businesses and entrepreneurs
- Online retailers

---

## 2. **Technologies Used**
- **Framework**: Django (Python)
- **Frontend**: Bootstrap, CSS
- **Database**: SQLite (Default Django configuration)
- **Other dependencies** (from `requirements.txt`):
  - asgiref==3.7.2
  - backports.zoneinfo==0.2.1
  - certifi==2024.8.30
  - charset-normalizer==3.4.0
  - Django==4.2.11
  - idna==3.10
  - pillow==10.2.0
  - requests==2.32.3
  - sqlparse==0.4.4
  - typing-extensions==4.10.0
  - urllib3==2.2.3

---

## 3. **Project Structure**
```plaintext
SilverGain/
├── SilverGain/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── store/
│   ├── forms/
│   ├── models/
│   ├── templates/
│   ├── views/
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
├── static/
│   ├── images/
│   ├── home.css
├── uploads/
│   ├── products/
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
```

### **Key Apps**
1. **Store App**: Handles all core functionalities, including models, views, templates, and forms related to products, categories, carts, and user accounts.

---

## 4. **Installation Guide**

### **System Requirements**
- Python 3.x
- Django 4.2.x
- SQLite (comes with Django)

### **Installation Steps**
1. **Clone the Repository**:
   ```bash
   git clone <repo-url>
   cd SilverGain
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (for accessing the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open a browser and visit `http://127.0.0.1:8000/`.

---

## 5. **Database Design**

### **Models**
1. **Cart**:
   - Fields: `product`, `quantity`, `user`
   - Relations: Each cart item relates to a user and a product.

2. **Category**:
   - Fields: `name`
   - Methods: `get_all_categories()` returns all categories.

3. **Customer**:
   - Fields: `first_name`, `last_name`, `phone`, `email`, `password`
   - Methods: `register()`, `get_customer_by_email(email)`, `isExists()`

4. **Order**:
   - Fields: `product`, `customer`, `quantity`, `price`, `address`, `phone`, `date`, `status`
   - Methods: `placeOrder()`, `get_orders_by_customer(customer_id)`

5. **Products**:
   - Fields: `image_url`, `image_file`, `name`, `price`, `category`, `description`, `quantity`
   - Methods: `get_all_products()`, `get_products_by_id(ids)`, `get_all_products_by_categoryid(category_id)`

6. **Reviews**:
   - Fields: `product`, `stars`, `comment`

### **Relationships**:
- **Product to Category**: Many-to-one
- **Product to Cart**: Many-to-many (through `Cart` model)
- **Order to Customer**: Many-to-one
- **Product to Reviews**: One-to-many

---

## 6. **Views and URLs**

### **Key Views**
1. **Cart**:
   - Adds products to the cart and handles quantity updates.
   - URL: `/add_to_cart/<int:product_id>/`

2. **Home**:
   - Displays a list of products and categories.
   - URL: `/home/`

3. **Landing Page**:
   - Displays two random products and allows users to browse all products.
   - URL: `/`

4. **Product Details**:
   - Shows detailed information about a single product, with related/similar products.
   - URL: `/products/<int:product_id>/`

5. **User Authentication**:
   - Handles user registration, login, and logout.
   - URLs: `/user-registration/`, `/user-login/`, `/user_logout/`

6. **Payment**:
   - Handles payment logic for products in the cart.
   - URL: `/payment/`

### **Admin Panel**:
Admins can manage:
- Products
- Categories
- Orders
- Customers
- Reviews
- Carts

---

## 7. **Templates**

### **Key Templates**:
1. **home.html**: Displays the home page with a list of products and categories.
2. **landing_page.html**: Displays two random products and allows browsing of all products.
3. **product_details.html**: Shows details of individual products.
4. **payment.html**: Handles product payment logic.
5. **user_registration.html**: User registration form.
6. **user_login.html**: User login form.

### **Template Inheritance**:
- **base.html**: Common base template for all other templates (header, footer, etc.).

---

## 8. **Forms**

### **UserLoginForm**:
- Fields: `email`, `password`
- Used for user authentication.

### **UserRegistrationForm**:
- Fields: `firstname`, `lastname`, `email`, `phone`, `password`
- Used for user sign-up.

---

## 9. **Authentication**

SilverGain uses Django's built-in authentication system for:
- User login and registration.
- Account management.
- Permissions for specific features (e.g., cart, payments).

Third-party authentication for services like Google and Facebook can be integrated using Django's authentication plugins.

---

## 10. **Static Files and Media**

### **CSS**:
- **home.css**: Provides the general styling for the web application.

### **Media**:
- Product images are stored in the `uploads/products/` directory.

---

## 11. **API Integration**

SilverGain integrates with the FakeStore API to fetch products, allowing a broader range of product listings on the platform. The fetched products are stored in the database and displayed on the platform’s front end.

---

This documentation serves as a comprehensive guide for developers, users, and administrators to understand and work with SilverGain's e-commerce platform.