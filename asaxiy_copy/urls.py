# first one. DEPLOYED.
# 1.0
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail')
# ]


# LOGIN REGISTER LOGOUT.
# 2.0
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail'),
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'),
#     path('logout/', views.logout_view, name='logout'),
# ]


# Profil uchun.
# 3.0
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail'),
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'),
#     path('logout/', views.logout_view, name='logout'),
#     path('profile/', views.profile_view, name='profile'),
# ]


# Parolni o'zgartirish, yangilash, esdan chiqqanda o'zgartirish va validatsiya.
# 4.0
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('forgot-password/reset/', views.forgot_password_reset_view, name='forgot_password_reset'),
]