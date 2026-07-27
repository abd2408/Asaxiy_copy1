from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    artikul = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    # --- YANGI DINAMIK XOSSA ---
    @property
    def is_available(self):
        # Barcha filiallardagi umumiy sonini hisoblaydi
        total_stock = sum(stock.quantity for stock in self.stock_set.all())
        return total_stock > 0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)
    is_main = models.BooleanField(default=False)


class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryAttribute(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=500)


class Branch(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Stock(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True, null=True)
    storage = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default=0)


class CustomUser(models.Model):
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    passport = models.CharField(max_length=9, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=30)
    delivery_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=30)
    month_count = models.IntegerField(blank=True, null=True)
    monthly_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=30)
    paid_at = models.DateTimeField(blank=True, null=True)


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField()
    pros = models.TextField(blank=True)
    cons = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)