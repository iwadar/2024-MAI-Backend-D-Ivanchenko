from django.urls import path, include
from cheeseFactory.views import *

urls_list_cheese = [
    path('', listCheese, name='List of cheese'),
    path('cheese/', cheese, name='Cheese'),
    path('create', createCheese, name='New cheese'),
    path('search/', searchCheese, name='Search cheese'),
]

urls_order = [
    path('', orderHistory, name='History'),
    path('order/', order, name='Order'),
    path('create', createOrder, name='New Order'),
]

urlpatterns = [
    path('', welcomeToFactory, name='home'),
    path('profile/', profile, name='profile'),
    path('listCheese/', include(urls_list_cheese)),
    path('orderHistory/', include(urls_order)),
]
