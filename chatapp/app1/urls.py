from django.urls import path
from app1.views import HomeView, LoginView, RegisterView, ProtectedView, ChatView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path('protected/', ProtectedView.as_view(), name="protected"),
    path('chat/<int:pk>', ChatView.as_view(), name="chat")
]