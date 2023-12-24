from django.urls import path
from . import views

app_name = 'mh'
urlpatterns = [
    path('', views.index),
    path('customer_login/',views.customer_login),
    path('customer_register/',views.customer_register),
    path('homepage/',views.homepage),
    path('seller_register/',views.seller_register),
    path('seller_login/',views.seller_login),
    path('homepage1/',views.homepage1),
    path('individual_center/',views.individual_center),
    path('individual_center1/',views.individual_center1),
    path('image/',views.image),
    path('info/',views.info),
    path('change/',views.change),
    path('logout/',views.logout),
    path('list/',views.list),
    path('wallet/',views.wallet),
    path('add/',views.add),
    path('shop/',views.shop),
    path('add_goods/',views.add_goods),
    path('good_change/',views.good_change)
]