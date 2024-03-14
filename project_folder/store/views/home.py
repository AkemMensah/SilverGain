from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Home_view(View):

	def post(self, request):
		# Retrieve the value of the 'product' parameter from the POST request data
		product = request.POST.get('product')
		# Retrieve the value of the 'remove' parameter from the POST request data
		remove = request.POST.get('remove')
		# Retrieve the current shopping cart stored in the session data
		cart = request.session.get('cart')
		# check if cart exists
		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity <= 1:
						cart.pop(product)
					else:
						cart[product] = quantity-1
				else:
					cart[product] = quantity+1

			else:
				cart[product] = 1
		# if no cart
		else:
			cart = {}
			cart[product] = 1
			
        # Updates the session data with the modified cart
		request.session['cart'] = cart
		print('cart', request.session['cart'])
		# Redirect the user to the 'home' page after updating the cart
		return redirect('home')

	def get(self, request):
		# print()
		# Retrieve the full path of the current request, including the query parameters
		return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
	
def store(request):
		# get cart for session
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
		# Retrieve all available categories of products.
        categories = Category.get_all_categories()
		# Retrieves the category ID from the GET parameters in the request.
        categoryID = request.GET.get('category')
		# retrieve products belonging to that category
        if categoryID:
            products = Products.get_all_products_by_categoryid(categoryID)
        else:
            products = Products.get_all_products()

        # Prepare Data for Rendering
        data = {}
		# Add the retrieved products to the data dictionary
        data['products'] = products
		# Add the retrieved categories to the data dictionary
        data['categories'] = categories

        print('you are : ', request.session.get('email'))
		# render the 'home.html' template with the data dictionary.
        return render(request, 'home.html', data)
