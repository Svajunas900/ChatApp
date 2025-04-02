from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
  template_name = "index.html"


class LoginView(TemplateView):
  template_name = "registration/login.html"


class RegisterView(TemplateView):
  template_name = "registration/register.html"

  # def form_valid()