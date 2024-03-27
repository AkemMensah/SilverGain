from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from store.models.products import Products
from store.models.category import Category
from store.models.cart import Cart
from django.views import View


# Create your views here.
# @login_required
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
		# random products for slide
	product1 = Products.objects.order_by('?').first()
	product2 = Products.objects.order_by('?').first()
	product3 = Products.objects.order_by('?').first()
	data = {}
	cart_count = Cart.objects.filter(user=request.user).count()

	# Add the retrieved products to the data dictionary
	data['products'] = products
	data['product1']= product1
	data['product2']= product2
	data['product3']= product3
	data['cart_count'] = cart_count if cart_count else 0
	# Add the retrieved categories to the data dictionary
	data['categories'] = categories
	data['user'] = request.user

	print('you are : ', request.session.get('email'))
	# render the 'home.html' template with the data dictionary.
	# print("Data:", data)
	return render(request, 'home.html', data)
