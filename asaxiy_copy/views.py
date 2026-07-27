from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import CustomUser

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    # ID bo'yicha mahsulotni topadi, topilmasa 404 xatolik beradi
    product = get_object_or_404(Product, pk=pk)

    # Mahsulotga tegishli rasmlar va xususiyatlarni ham olishimiz mumkin:
    images = product.images.all()  # ProductImage related_name='images'
    attributes = product.productattributevalue_set.all()
    stocks = product.stock_set.all()
    reviews = product.review_set.all()

    context = {
        'product': product,
        'images': images,
        'attributes': attributes,
        'stocks': stocks,
        'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)