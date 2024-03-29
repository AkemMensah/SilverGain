"""
URL configuration for SilverGain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from store.views.home import Home_view,store
from store.views.products import product_list
from store.views.product_details import product_details
from store.views.cart import add_to_cart
from store.views.landing_page import landing_page
from store.views.user_registration import user_registration
from store.views.user_login import user_login
from store.views.logout import user_logout
from store.views.payment import payment
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('landing_page/',landing_page,name='landing_page'),
    path('products/',product_list, name='products'),
    path('user-registration/',user_registration, name='user_registration'),
    path('user-login/',user_login,name="user_login"),
    path('user_logout/',user_logout,name='user_logout'),
    path('accounts/login/',user_login,name="user_login"),
    path('payment/', payment,name="payment"),
    path('products/<int:product_id>/',product_details, name='product_details'),
    path('', Home_view.as_view(),name='store'),
    path('store', store, name='store'),
    path('admin/', admin.site.urls),
]

urlpatterns+=staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
