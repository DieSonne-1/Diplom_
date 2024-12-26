"""
Создадим представления для обработки запросов входа, регистрации и выхода
Также создаём представления для отображения главной страницы и страницы магазина
"""

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from .models import Product


# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')


def register_user(request):
    """Функция обрабатывает запрос регистрации"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # Создаётся экземпляр формы с переданными данными
        if form.is_valid():
            # Если форма валидна, новый пользователь сохраняется в базе данных
            # и перенаправляется на страницу входа
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})


def login_user(request):
    """Функция обрабатывает запрос входа пользователя"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # Создаётся экземпляр формы с переданными данными
        if form.is_valid():
            # Если форма валидна, извлекаются имя и пароль, и выполняется аутентификация
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Если аутентификация успешна, выполняется вход
                # и перенаправление на следующую страницу
                login(request, user)
                return redirect('shop')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    """Функция обрабатывает запрос завершения сессии"""
    logout(request)
    # Вызывается функция для выхода пользоателя и перенаправляет его на страницу входа
    return redirect('login')


def product_list(request):
    """Отправляем запрос к базе данных для получения всех продуктов"""
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    # Создаём экзэмпляр класса и задаём колличество объектов на странице
    # Делаем GET запрос, получаем номер и текущую страницу
    page_obj = paginator.get_page(page_number)
    # Передаём данные в шаблон
    return render(request, 'shop.html', {'products': products,
                                         'page_obj': page_obj})

