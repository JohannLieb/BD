from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    products_controller,
    RegisterController,
    LoginController,
    LogoutController,
    ProfileController,
    OrderController,
    ProfChangeController,
    NewOrderController
)

urlpatterns = [
    path(r'', products_controller, name='main'),
    path(r'register', RegisterController.as_view(), name='register'),
    path(r'products', products_controller, name='products'),
    path(r'login', LoginController.as_view(), name='login'),
    path(r'logout', login_required(login_url='/login')(LogoutController.as_view()), name='login'),
    path(r'profile', login_required(login_url='/login')(ProfileController.as_view()), name='profile'),
    path(r'orders', login_required(login_url='/login')(OrderController.as_view()), name='orders'),
    path(r'profchange', login_required(login_url='/login')(ProfChangeController.as_view()), name='profchange'),
    path(r'orders/new', login_required(login_url='/login')(NewOrderController.as_view()), name='new_order')

]

