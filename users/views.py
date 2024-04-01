from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required()
def logout_page(request):
    logout(request)
    messages.success(request, "tizimdan chiqdingiz")
    return redirect('common:index')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        if not CustomUser.objects.filter(phone_number=username).exists():
            print("not exists")
            messages.error(request, "User Does not exists")
            return render(request, 'login.html')
        user = authenticate(phone_number=username, password=password)
        print(user)
        if user:
            login(request, user)
            print("login")
            messages.success(request, "you are succes login")
            return redirect('common:index')

    return render(request, 'login.html')


def sign_up_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        print(username, 1)
        print(password, 1)
        if CustomUser.objects.filter(phone_number=username).exists():
            messages.error(request, "bu user mavjud")
            return render(request, 'sign-up.html')
        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "User yaratildi")
        return redirect('login_page')
    return render(request, 'sign-up.html')


def profile(request):
    return render(request, 'user-profile.html')