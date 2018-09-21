from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.urls import reverse
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})



def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, "registration/change_password.html", {"form": form})
