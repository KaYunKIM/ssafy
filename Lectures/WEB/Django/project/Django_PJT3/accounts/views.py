from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    else:
        if request.method=='POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('community:index')
        else:
            form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    else:
        if request.method=='POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'community:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)

@require_POST
@login_required
def logout(request):
    auth_logout(request)
    return redirect('community:index')

@require_POST
@login_required
def delete_user(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    if user == request.user:
        user.delete()
    return redirect('accounts:signup')

def detail(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)