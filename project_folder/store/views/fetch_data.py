# import requests
# from store.models.products import Products, Category
# import logging

# logger = logging.getLogger(__name__)

# def fetch_and_save_products():
#     api_url = "https://fakestoreapi.com/products"
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         products_data = response.json()

#         # Save products to the database
#         for product in products_data:
#             category, created = Category.objects.get_or_create(name=product['category'])

#             # Avoid duplicating products if they already exist
#             product_obj, created = Products.objects.get_or_create(
#                 name=product['title'],
#                 defaults={
#                     'price': product['price'],
#                     'description': product['description'],
#                     'image': product['image'],
#                     'category': category,
#                     'quantity': product.get('count', 1000),  # Default to 1000 if 'count' isn't provided
#                 }
#             )

#     except requests.exceptions.RequestException as e:
#         logger.error(f"Error fetching products: {e}")
