from django.urls import path

from . import views

app_name = 'API'
urlpatterns = [
    path('authLogin/', views.authLogin),
    path('signUp/', views.signUp),
    path('orders/', views.orders),
    path('getCart/<str:email>/', views.getCart),
    path('pushCart/', views.pushCart),
    path('getMenu/', views.getMenu)
]