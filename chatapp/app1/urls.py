from django.urls import path
from app1.views import HomeView, LoginView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register")
]