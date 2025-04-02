from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, DetailView
from app1.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from app1.admin import Conversation
# Create your views here.

class HomeView(TemplateView):
  template_name = "index.html"


class LoginView(FormView):
  template_name = "registration/login.html"
  form_class = UserLoginForm
  success_url = "/"

  def form_valid(self, form):
    username = form.cleaned_data["username"]
    password = form.cleaned_data["password"]
    try: 
      user = User.objects.get(username=username)
      authenticate(username=username, password=password)
      login(self.request, user)
      return super().form_valid(form)
    except User.DoesNotExist:
      form.add_error('email', "User with this email doesn't exist")
    return super().form_invalid(form)

class RegisterView(FormView):
  template_name = "registration/register.html"
  form_class = UserRegisterForm
  success_url = "/"

  def form_valid(self, form):
    email = form.cleaned_data["email"]
    username = form.cleaned_data["username"]
    password = form.cleaned_data["password"]
    confirm_password = form.cleaned_data["confirm_password"]
    try: 
      user = User.objects.get(email=email)
      form.add_error('email', 'User with this email already exists')
      return self.form_invalid(form)
    except User.DoesNotExist:
      if password != confirm_password:
        form.add_error('password', "Passwords don't match")
        return self.form_invalid(form)
      new_user = User.objects.create(email=email, username=username)
      new_user.set_password(password)
      new_user.save()
      authenticate(username=new_user.username,password=new_user.password)
      login(self.request, new_user)
    return super().form_valid(form)


class ProtectedView(LoginRequiredMixin, TemplateView):
  template_name = "protected.html"


class ChatView(LoginRequiredMixin, DetailView):
  template_name = "chat.html"
  model = Conversation
  context_object_name = "conversation"
  
  
  def get(self, request, *args, **kwargs):
    response = super().get(request, *args, **kwargs)
    response.set_cookie('user_id', self.request.user.id, max_age=60*60*24)  
    return response


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)  
    conversation = self.get_object()
    context['messages'] = conversation.messages.all().order_by('created_at')
    context['username'] = self.request.user.username
    print(self.request.user.id)
    return context
  