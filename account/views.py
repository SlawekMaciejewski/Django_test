from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import LogInForm, UserProfile, UserForm, UserProfileForm


# Create your views here.
@login_required
def modify_user(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user,
                             data=request.POST)
        profile_form = UserProfileForm(instance=request.user.userprofile,
                                       data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('my_account')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'account/modify_user.html',
                  {'user_form': user_form, 'profile_form': profile_form})


class MyUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = UserProfile.objects.create(user=user)
            profile.save()
        return user


class SignUp(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


class UserView(TemplateView):
    template_name = 'account/my_account.html'


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnianie pomyślne')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Nieprawidłowe dane')
    else:
        form = LogInForm()
    return render(request, 'account/login.html', {'form': form})
