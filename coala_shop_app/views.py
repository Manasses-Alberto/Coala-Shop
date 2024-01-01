from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from coala_shop_app.models import Product, Shoppings
from datetime import datetime

def home(request):
    return render(request, 'index.html', {'products': Product.objects.all()})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'products': Product.objects.all(), 'login': True, 'register': False})

    elif request.method == 'POST':
        email = request.POST['email'].strip().lower()
        password = request.POST['password']
        try:
            username = User.objects.get(email=email)

        except User.DoesNotExist:
            return render(request, 'login.html', {'login': True, 'error': True, 'field_error': ['email'], 'message': 'O seu email está inválido. Tente novamente'})

        else:
            user = authenticate(request, username=username, password=password)
            try:
                auth_login(request, user)
            
            except AttributeError:
                return render(request, 'login.html', {'login': True, 'error': True, 'field_error': ['password'], 'message': 'A sua senha está inválida. Tente novamente'})

            else:
                return redirect('home')

@login_required(login_url='/auth/login/')
def logout(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'register': True})

    elif request.method == 'POST':
        first_name = request.POST['first-name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password_conf = request.POST['password-confirmation']
        old_username = User.objects.filter(username=f'{first_name.strip().title()} {surname.strip().title()}').first()
        old_email = User.objects.filter(email=email.strip().lower()).first()
        if not first_name.isalpha():
            return render(request, 'register.html', {'error': True, 'field_error': ['first_name'], 'message': 'O primeiro nome é inválido não inclua símbolos, números ou espaços...', 'register': True})

        elif not surname.isalpha():
            return render(request, 'register.html', {'error': True, 'field_error': ['surname'], 'message': 'O sobrenome é inválido não inclua símbolos, números ou espaços...', 'register': True})

        elif old_username:
            return render(request, 'register.html', {'error': True, 'field_error': ['first_name', 'surname'], 'message': 'O sistema já encontrou outro usuário com esses nomes...', 'register': True})

        elif old_email:
            return render(request, 'register.html', {'error': True, 'field_error': ['email'], 'message': 'O sistema já encontrou outro usuário com esse email...', 'register': True})

        elif password != password_conf:
            return render(request, 'register.html', {'error': True, 'field_error': ['password', 'password-confirmation'], 'message': 'Verifique as senhas estão diferentes...', 'register': True})

        else:
            new_user = User.objects.create_user(first_name=first_name.strip().title(), last_name=surname.strip().title(), username=f'{first_name.strip().title()} {surname.strip().title()}', email=email.strip().lower(), password=password)
            new_user.save()
            user = authenticate(request, username=f'{first_name.strip().title()} {surname.strip().title()}', password=password)
            auth_login(request, user)
            return redirect('home')

@login_required(login_url='/auth/login/')
def add_buy(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    new_shopping = Shoppings.objects.create(buyer=request.user, product=product, date=datetime.today().now())
    new_shopping.save()
    return redirect('home')

@login_required(login_url='/auth/login/')
def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product-details.html', {'product': product})
