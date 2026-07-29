# First version/ DEPLOYED
# 1.0
# from django.shortcuts import render, get_object_or_404
# from .models import Product
# from .models import CustomUser
#
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})
#
# def product_detail(request, pk):
#     # ID bo'yicha mahsulotni topadi, topilmasa 404 xatolik beradi
#     product = get_object_or_404(Product, pk=pk)
#
#     # Mahsulotga tegishli rasmlar va xususiyatlarni ham olishimiz mumkin:
#     images = product.images.all()  # ProductImage related_name='images'
#     attributes = product.productattributevalue_set.all()
#     stocks = product.stock_set.all()
#     reviews = product.review_set.all()
#
#     context = {
#         'product': product,
#         'images': images,
#         'attributes': attributes,
#         'stocks': stocks,
#         'reviews': reviews,
#     }
#     return render(request, 'product_detail.html', context)


# Login Register logout lar qo'shildi.
# 2.0
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.hashers import make_password, check_password
# from .models import Product, CustomUser
# from .forms import LoginForm, RegisterForm
#
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product_list.html', {'products': products})
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     images = product.images.all()
#     attributes = product.productattributevalue_set.all()
#     stocks = product.stock_set.all()
#     reviews = product.review_set.all()
#
#     context = {
#         'product': product,
#         'images': images,
#         'attributes': attributes,
#         'stocks': stocks,
#         'reviews': reviews,
#     }
#     return render(request, 'product_detail.html', context)
#
#
# def login_view(request):
#     error = None
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             phone = form.cleaned_data['phone']
#             password = form.cleaned_data['password']
#             try:
#                 user = CustomUser.objects.get(phone=phone)
#                 if check_password(password, user.password):
#                     request.session['user_id'] = user.id
#                     return redirect('product_list')
#                 else:
#                     error = "Telefon raqam yoki parol noto'g'ri."
#             except CustomUser.DoesNotExist:
#                 error = "Bunday foydalanuvchi topilmadi."
#     else:
#         form = LoginForm()
#
#     return render(request, 'login.html', {'form': form, 'error': error})
#
#
# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             phone = form.cleaned_data['phone']
#
#             if CustomUser.objects.filter(phone=phone).exists():
#                 return render(request, 'register.html', {
#                     'form': form,
#                     'error': "Bu telefon raqam bilan foydalanuvchi allaqachon mavjud."
#                 })
#
#             user = CustomUser.objects.create(
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 phone=phone,
#                 email=form.cleaned_data['email'],
#                 password=make_password(form.cleaned_data['password']),
#             )
#             request.session['user_id'] = user.id
#             return redirect('product_list')
#     else:
#         form = RegisterForm()
#
#     return render(request, 'register.html', {'form': form})
#
#
# def logout_view(request):
#     request.session.flush()
#     return redirect('login')


# Profil qo'shildi.
# 3.0
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib import messages
# from .models import Product, CustomUser
# from .forms import LoginForm, RegisterForm, ProfileForm
#
# def product_list(request):
#     products = Product.objects.all()
#
#     user = None
#     user_id = request.session.get('user_id')
#     if user_id:
#         user = CustomUser.objects.filter(id=user_id).first()
#
#     return render(request, 'product_list.html', {'products': products, 'user': user})
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     images = product.images.all()
#     attributes = product.productattributevalue_set.all()
#     stocks = product.stock_set.all()
#     reviews = product.review_set.all()
#
#     context = {
#         'product': product,
#         'images': images,
#         'attributes': attributes,
#         'stocks': stocks,
#         'reviews': reviews,
#     }
#     return render(request, 'product_detail.html', context)
#
#
# def login_view(request):
#     error = None
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             phone = form.cleaned_data['phone']
#             password = form.cleaned_data['password']
#             try:
#                 user = CustomUser.objects.get(phone=phone)
#                 if check_password(password, user.password):
#                     request.session['user_id'] = user.id
#                     return redirect('product_list')
#                 else:
#                     error = "Telefon raqam yoki parol noto'g'ri."
#             except CustomUser.DoesNotExist:
#                 error = "Bunday foydalanuvchi topilmadi."
#     else:
#         form = LoginForm()
#
#     return render(request, 'login.html', {'form': form, 'error': error})
#
#
# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             phone = form.cleaned_data['phone']
#
#             if CustomUser.objects.filter(phone=phone).exists():
#                 return render(request, 'register.html', {
#                     'form': form,
#                     'error': "Bu telefon raqam bilan foydalanuvchi allaqachon mavjud."
#                 })
#
#             user = CustomUser.objects.create(
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 phone=phone,
#                 email=form.cleaned_data['email'],
#                 password=make_password(form.cleaned_data['password']),
#             )
#             request.session['user_id'] = user.id
#             return redirect('product_list')
#     else:
#         form = RegisterForm()
#
#     return render(request, 'register.html', {'form': form})
#
#
# def logout_view(request):
#     request.session.flush()
#     return redirect('login')
#
#
# def profile_view(request):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         return redirect('login')
#
#     user = get_object_or_404(CustomUser, id=user_id)
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Ma'lumotlar saqlandi.")
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=user)
#
#     return render(request, 'profile.html', {'form': form, 'user': user})


# Parolni o'zgartirish, yangilash, esdan chiqqanda o'zgartirish va validatsiya.
# 4.0
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Product, CustomUser
from .forms import (
    LoginForm, RegisterForm, ProfileForm,
    ChangePasswordForm, ForgotPasswordIdentifyForm, SetNewPasswordForm
)


def product_list(request):
    products = Product.objects.all()
    user = None
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.filter(id=user_id).first()
    return render(request, 'product_list.html', {'products': products, 'user': user})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    images = product.images.all()
    attributes = product.productattributevalue_set.all()
    stocks = product.stock_set.all()
    reviews = product.review_set.all()
    context = {
        'product': product, 'images': images, 'attributes': attributes,
        'stocks': stocks, 'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)


def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(phone=phone)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    return redirect('product_list')
                else:
                    error = "Telefon raqam yoki parol noto'g'ri."
            except CustomUser.DoesNotExist:
                error = "Bunday foydalanuvchi topilmadi."
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'error': error})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if CustomUser.objects.filter(phone=phone).exists():
                return render(request, 'register.html', {
                    'form': form,
                    'error': "Bu telefon raqam bilan foydalanuvchi allaqachon mavjud."
                })
            user = CustomUser.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=phone,
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),
            )
            request.session['user_id'] = user.id
            return redirect('product_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    request.session.flush()
    return redirect('product_list')


def profile_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumotlar saqlandi.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form, 'user': user})


def change_password_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            if not check_password(old_password, user.password):
                form.add_error('old_password', "Eski parol noto'g'ri.")
            else:
                user.password = make_password(form.cleaned_data['new_password'])
                user.save()
                messages.success(request, "Parol muvaffaqiyatli o'zgartirildi.")
                return redirect('profile')
    else:
        form = ChangePasswordForm()

    return render(request, 'change_password.html', {'form': form})


def forgot_password_view(request):
    error = None
    if request.method == 'POST':
        form = ForgotPasswordIdentifyForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            user = CustomUser.objects.filter(phone=identifier).first() \
                or CustomUser.objects.filter(email=identifier).first()
            if user:
                request.session['reset_user_id'] = user.id
                return redirect('forgot_password_reset')
            else:
                error = "Bunday telefon raqam yoki email bilan foydalanuvchi topilmadi."
    else:
        form = ForgotPasswordIdentifyForm()
    return render(request, 'forgot_password.html', {'form': form, 'error': error})


def forgot_password_reset_view(request):
    reset_user_id = request.session.get('reset_user_id')
    if not reset_user_id:
        return redirect('forgot_password')

    user = get_object_or_404(CustomUser, id=reset_user_id)

    if request.method == 'POST':
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            user.password = make_password(form.cleaned_data['new_password'])
            user.save()
            del request.session['reset_user_id']
            messages.success(request, "Parol muvaffaqiyatli o'zgartirildi. Endi tizimga kiring.")
            return redirect('login')
    else:
        form = SetNewPasswordForm()

    return render(request, 'forgot_password_reset.html', {'form': form})