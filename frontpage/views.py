from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from .models import Clients
from .models import Product, Clients, Staff
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def products_controller(request):
    return render(request, 'main.html', { 'product': Product.objects.all()  })


class RegisterController(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username, password = request.POST['login'], request.POST['password']
        if Clients.objects.filter(login=username).all():
            return render(request, "register.html", { 'result': 'User with such login already exists.'}, status=400)
        if Staff.objects.filter(login=username).all():
            return render(request, "register.html", { 'result': 'User with such login already exists.'}, status=400)
        hashed_password = make_password(password)
        new_client = Clients.objects.create(login=username, userpass=hashed_password)
        new_client.save()
        return render(request, 'register.html', { 'result': 'Successfully registered!'})




class LoginController(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username, password = request.POST['login'], request.POST['password']
        new_client = Clients.objects.get(login=username)
        is_password_valid = check_password(request.POST['password'], new_client.userpass )
        if is_password_valid:
            request.session.user = new_client
            return render(request, 'main.html', {'result': 'Welcome!'})
        else:
            return render(request, 'main.html', {'error': 'Логин/пароль введен неверно!'})



class LogoutController(View):
    def get(self, request):
        if request.session.user:
            request.session.user = None
        return render(request, "index.html")

def register_controller(request):
    return render(request, 'register.html')


def logout1(request):
    logout(request)
    render(request, "index.html", {'user': new_client})