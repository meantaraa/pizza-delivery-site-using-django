from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(PizzaCategory)
admin.site.register(Pizza)
admin.site.register(Cart)
admin.site.register(CartItem)