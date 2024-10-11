from django.shortcuts import render
import requests
from django.views import View
from store.models.products import Products, Category
import logging

logger = logging.getLogger(__name__)

def fetch_and_save_products():
    api_url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        products_data = response.json()

        # Save products to the database
        for product in products_data:
            category, created = Category.objects.get_or_create(name=product['category'])

            # Avoid duplicating products if they already exist
            product_obj, created = Products.objects.get_or_create(
                name=product['title'],
                defaults={
                    'price': product['price'],
                    'description': product['description'],
                    'image_url': product['image'],
                    'category': category,
                    'quantity': product.get('count', 1000),  # Default to 1000 if 'count' isn't provided
                }
            )

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching products: {e}")

def landing_page(request):
    # Fetch and save products from the external API if the database is empty
    # if not Products.objects.exists():
    fetch_and_save_products()

    # Fetch two distinct random products
    products = Products.objects.order_by('?')[:2]
    if len(products) >= 2:
        product1, product2 = products[0], products[1]
    else:
        product1 = product2 = None

    # Fetch all or a limited number of products (e.g., 10)
    all_products = Products.objects.all()#[:10]

    user = request.user if request.user.is_authenticated else None
    return render(request, 'landing_page.html', {
        "product1": product1,
        "product2": product2,
        "products": all_products,
        "user": user
    })
