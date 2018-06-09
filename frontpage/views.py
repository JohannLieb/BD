from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from django.views.generic import  TemplateView
from .models import Product, Clients, Staff, Orders, Property
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.utils import timezone

from decimal import Decimal

# Create your views here.
def products_controller(request):
    return render(request, 'main.html', { 'product': Product.objects.all()  })


class RegisterController(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username, password = request.POST['login'], request.POST['password']
        if any((Clients.objects.filter(login=username).all(),
                Staff.objects.filter(login=username).all(),
                User.objects.filter(username=username).all())):
            return render(request, "register.html", { 'result': 'User with such login already exists.'}, status=400)
        hashed_password = make_password(password)
        user = Clients.objects.create(login=username, userpass=hashed_password)
        user.save()
        return render(request, 'register.html', { 'result': 'Successfully registered!'})

class LoginController(View):

    def get(self, request):
        if request.user and request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')

    def post(self, request):
        username, password = request.POST['login'], request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'result': 'User doesn\'t exist or password is incorrect.'})

class LogoutController(View):

    def get(self, request):
        logout(request)
        return redirect('/')

class ProfileController(View):

    def get(self, request):
        return render(request, 'profile.html')


class OrderController(View):

    def get(self, request):
        orders = Orders.objects.filter(clients_id = request.user.clients_id)
        return render(request, 'orders.html', {'orders': orders})

class ProfChangeController(View):

    def get(self, request):
        logged_in_user = Clients.objects.get(clients_id=request.user.clients_id)
        phone_number = logged_in_user.telno
        address = logged_in_user.address
        fullname = logged_in_user.humanized_full_name
        return render(request, 'profchange.html', {'phone_number': phone_number,
                                                   'address': address, 'fullname': fullname} )


    def post(self, request):
        address, fullname, telno = request.POST['address'], request.POST['fullname'], request.POST['telno']
        logged_in_user = Clients.objects.get(clients_id=request.user.clients_id)
        logged_in_user.address = address
        logged_in_user.fullname = logged_in_user.cast_to_shitty_type(fullname)
        logged_in_user.telno = telno
        logged_in_user.save()
        # profchange = Clients(address=address, fullname=fullname, telno=telno)
        # profchange.save()
        # Тут ты создаёшь НОВОГО клиента
        return render(request, 'profchange_done.html')

class NewOrderController(View):

    def get(self, request):
        products = Product.objects.prefetch_related('characteristics_set__property').all()
        for product in products:
            for c in product.characteristics_set.all():
                if c.property.name == 'Price':
                    product.price = c.property.value
        return render(request, 'new_order.html', {'products': products})

    def post(self, request):
        product_id, client_id, price, description = request.POST['product_id'], request.user.clients_id, request.POST['price'], request.POST['description']
        new_order = Orders(orders_date=timezone.now(), description=description, product=Product.objects.get(product_id=int(product_id)),
                           clients=request.user, price=Decimal(price), paid=False)
        new_order.save()
        return render(request, 'order_done.html')