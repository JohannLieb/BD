from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from .models import Clients
from .models import Product, Clients, Staff

# Create your views here.
def products_controller(request):
    return render(request, 'main.html', { 'product': Product.objects.all()  })

class RegisterController(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username, password = request.POST['login'], request.POST['password']
        if Clients.objects.filter(login=username).all():
            return render(request, "register.html", { 'error': 'User with such login already exists.'}, status=400)
        if User.objects.filter(username=username).all():
            return render(request, "register.html", { 'error': 'User with such login already exists.'}, status=400)
        if Staff.objects.filter(username=username).all():
            return render(request, "register.html", { 'error': 'User with such login already exists.'}, status=400)
        new_client = Clients(login=username, userpass=password)
        return HttpResponse(status=400)



def register_controller(request):
    return render(request, 'register.html')

def entry_controller(request):
    return render(request, 'entry.html')
