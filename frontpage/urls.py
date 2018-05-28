from django.urls import path
from .views import (
    products_controller,
    RegisterController,
    LoginController,
    LogoutController,
    logout
)

urlpatterns = [
    path(r'', products_controller, name='main'),
    path(r'register', RegisterController.as_view(), name='register'),
    path(r'products', products_controller, name='products'),
    path(r'login', LoginController.as_view(), name='login'),
    path(r'logout', LogoutController.as_view(), name='login'),
    path(r'logout', logout, name='login'),

]

