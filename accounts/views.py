from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.views.generic import CreateView
from .forms import SignUpForm, LoginForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    #afisez formularul
    def get(self, request):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    #procesez SignUpForm si redirectionez login
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        return render(request, 'accounts/signup.html', {'form': form})

#login in functie de rol admin/manager->admin site user->devize
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                #redirectionz în functie de rol:
                if user.role in ('admin','manager'):
                    return redirect('admin:index')
                return redirect('estimates:list_devize')
        return render(request, 'accounts/login.html', {'form': form, 'error': 'Date invalide'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')

class ProfileView(LoginRequiredMixin, View):
    #afisez ProfileForm
    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, 'accounts/profile.html', {'form': form})
    #salveaza modificarile profilului
    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        return render(request, 'accounts/profile.html', {'form': form})
