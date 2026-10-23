from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('shop',views.shop,name='shop'),
    path('buy/<int:product_id>',views.buy_now,name='buy_now'),
    path('order-success',views.order_success,name='order_success')
]