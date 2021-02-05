from django.contrib import admin
# user name: vinay
# password: vinay@1436
# Register your models here.
from .models import Product, Contact, Order, OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
