from django.contrib import admin

from cheeseFactory.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Cheese)
admin.site.register(Order)
admin.site.register(List_cheese)
