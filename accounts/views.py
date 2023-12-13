from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ads.models import Ads
from .forms import Userform, Profileform, EditUserform
from .models import Profile

@login_required(login_url='login')
def user_ads(request):
    ads = Ads.objects.filter(user = request.user)
    context = {
        'context_ads': ads,
    }
    return render(request, 'user_ads.html', context)

def SignUpUser(request):
    if request.method == 'POST':
        user_form = Userform(request.POST)
        
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if user.password == request.POST.get('password2'):
                user.set_password(user.password)
                user_form.save()
                Profile.objects.create(user=user)
                messages.success(request, 'Вы успешно зарегистрировались')
                # path("signin/", SigninUser, name = "login")
                return redirect('login')
            else:
                messages.error(request, 'Пароли не совпадают')
                # path("signup/", SignupUser, name = "register")
                return redirect('register')
        else:
            messages.error(request, 'Ошибка регистрации. Попробуйте снова')
            return redirect('register')
        
    else:
        user_form = Userform()
        return render(request, 'register.html', {'contex_form': user_form})
    

def SignInUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
                user = authenticate(request=request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Вы успешно вошли!')
                    return redirect("home")
                else:
                        messages.error(request, 'Неверное имя пользователя или пароль.')
        elif username:
            messages.warning(request, 'Пожалуйста введите пароль.')
            return redirect("login")
        elif password:
            messages.warning(request, 'Пожалуйста, введите имя пользователя.')
            return redirect("login")
            
        else:
            messages.warning(request, 'Пожалуйста, введите имя пользователя и пароль.')
            return redirect("login")
    return render(request, "login.html")

def SignOutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Вы успешно вышли из учётной записи')
        return redirect('home')
    else:
        messages.error(request, 'Вы не авторизованы')
        return redirect('home')
    
@login_required(login_url='login')
def UserProfile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)     
    context = {
        'user_context': user,
        'profile_context': profile,        
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def EditProfile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        user_form = EditUserform(request.POST, instance=user)
        profile_form = Profileform(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль обновлён')
            return redirect('profile', user_id=user.id)
        else:
            messages.error(request, 'Ошибка редактирования профиля')
            return redirect('profile', user_id=user.id)
    else:
        user_form = EditUserform(instance=user)
        profile_form = Profileform(instance=profile)
        
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
    }
    return render(request, 'edit_profile.html', context)