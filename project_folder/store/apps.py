from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    # def ready(self):
        # Import the function to fetch and save products
        # from store.views.fetch_data import fetch_and_save_products
        
        # Fetch and save products on startup in both production and development
        # fetch_and_save_products()
