from django.contrib import admin
from .models import Product, Discount, OrderItem, Order, Category
# Register your models here.


admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)