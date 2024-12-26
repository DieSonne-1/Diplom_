"""
Используем встроенные формы Django, чтобы настроить аутентификацию.
Создадим поля для входа и регистрации.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """Форма наследуется от встроенной формы UserCreationForm и добавляет дополнительное поле email"""
    email = forms.EmailField(required=True)

    class Meta:
        """Указываем модель User и поля, которые нужно включить в форму"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
