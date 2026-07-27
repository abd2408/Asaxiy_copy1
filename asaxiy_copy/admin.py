from django.contrib import admin
from .models import (
    Category, Brand, Product, ProductImage, Attribute,
    CategoryAttribute, ProductAttributeValue, Branch, Stock,
    CustomUser, Address, Order, OrderItem, Payment, Review
)

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Attribute)
admin.site.register(CategoryAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(Branch)
admin.site.register(Stock)
admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Review)