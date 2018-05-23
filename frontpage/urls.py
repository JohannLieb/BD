from django.urls import path
from .views import (
    products_controller,
    register_controller,
    RegisterController
)

urlpatterns = [
    path('', products_controller,),
    # path('register', register_controller),
    path('register', RegisterController.as_view()),
    path('products', products_controller),
]

