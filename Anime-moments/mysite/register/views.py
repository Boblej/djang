from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.http import response

class Register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register/register.html'

    def formCookies(self, form):
        resource = super().fromCookies(form)
        response.set_cookie('registration_success', 'true', max_age=60*60*24*14)
        return response