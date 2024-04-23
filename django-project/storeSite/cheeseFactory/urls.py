from django.urls import path
from cheeseFactory.views import *

urlpatterns = [
    path('', welcomeToFactory, name='home'),
    path('listCheese/', listCheese, name='cheese'),
    path('purchaseHistory/', purchaseHistory, name='history'),
    path('order/', order, name='order'),
    path('profile/', profile, name='profile'),
]
