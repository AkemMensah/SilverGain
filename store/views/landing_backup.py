from django.shortcuts import render
import requests
from django.views import View
from store.models.products import Products, Category

def fetch_and_save_products():
    # API URL for fetching external products (use your actual API URL)
    api_url = "https://fakestoreapi.com/products"  # Example API
    try:
        # Fetching the external data
        response = requests.get(api_url)
        response.raise_for_status()
        products_data = response.json()

        # Save the products into the database
        for product in products_data:
            # Assuming the external API provides 'title', 'price', 'description', 'image', and 'category'
            # Match the fields with your Products model
            category, created = Category.objects.get_or_create(name=product['category'])  # Handling category

            Products.objects.create(
                name=product['title'],
                price=product['price'],
                description=product['description'],
                image=product['image'],
                category=category,
                quantity=product['count']  
            )

    except requests.exceptions.RequestException as e:
        print(f"Error fetching products: {e}")

def landing_page(request):
    product1 = Products.objects.order_by('?').first()
    product2 = Products.objects.order_by('?').first()
    products = Products.objects.all()
    user = request.user if request.user.is_authenticated else None
    return render(request, 'landing_page.html',{"product1":product1,"product2":product2,"products":products,"user":user})