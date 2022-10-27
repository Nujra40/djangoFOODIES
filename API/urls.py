from django.urls import path

from . import views

app_name = 'API'
urlpatterns = [
    path('authLogin/<str:email>/<str:password>', views.authLogin),
    path('signUp/', views.signUp)
]