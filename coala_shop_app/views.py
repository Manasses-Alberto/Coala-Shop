from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        email = request.POST['email'].strip().lower()
        password = request.POST['password']
        try:
            username = User.objects.get(email=email)

        except User.DoesNotExist:
            return render(request, 'login.html', {'error': True, 'field_error': ['email'], 'message': 'O seu email está inválido. Tente novamente'})

        else:
            user = authenticate(request, username=username, password=password)
            try:
                auth_login(request, user)
            
            except AttributeError:
                return render(request, 'login.html', {'error': True, 'field_error': ['password'], 'message': 'A sua senha está inválida. Tente novamente'})

            else:
                return redirect('home')

@login_required(login_url='/auth/login/')
def logout(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    
    elif request.method == 'POST':
        first_name = request.POST['first-name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password_conf = request.POST['password-confirmation']
        old_username = User.objects.filter(username=f'{first_name.strip().title()} {surname.strip().title()}').first()
        old_email = User.objects.filter(email=email.strip().lower()).first()
        if not first_name.isalpha():
            return render(request, 'register.html', {'error': True, 'field_error': ['first_name'], 'message': 'O primeiro nome é inválido não inclua símbolos, números ou espaços...'})

        elif not surname.isalpha():
            return render(request, 'register.html', {'error': True, 'field_error': ['surname'], 'message': 'O sobrenome é inválido não inclua símbolos, números ou espaços...'})

        elif old_username:
            return render(request, 'register.html', {'error': True, 'field_error': ['first_name', 'surname'], 'message': 'O sistema já encontrou outro usuário com esses nomes...'})

        elif old_email:
            return render(request, 'register.html', {'error': True, 'field_error': ['email'], 'message': 'O sistema já encontrou outro usuário com esse email...'})

        elif password != password_conf:
            return render(request, 'register.html', {'error': True, 'field_error': ['password', 'password-confirmation'], 'message': 'Verifique as senhas estão diferentes...'})

        else:
            new_user = User.objects.create_user(first_name=first_name.strip().title(), last_name=surname.strip().title(), username=f'{first_name.strip().title()} {surname.strip().title()}', email=email.strip().lower(), password=password)
            new_user.save()
            user = authenticate(request, username=f'{first_name.strip().title()} {surname.strip().title()}', password=password)
            auth_login(request, user)
            return redirect('home')
