from django import forms


class UserLoginForm(forms.Form):
  username = forms.CharField(min_length=8, max_length=50, label="Username", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(min_length=8, max_length=50, label="Password", required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    

class UserRegisterForm(forms.Form):
  email = forms.EmailField(min_length=10, max_length=50, label="Email address", required=True, widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Adress"}))
  username = forms.CharField(min_length=8, max_length=50, label="Username", required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(min_length=8, max_length=50, label="Password", required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
  confirm_password = forms.CharField(min_length=8, max_length=50, label="Confirm Password", required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}))
    