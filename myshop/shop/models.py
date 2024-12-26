"""
Создаём модель продукта в базе данных
Определяем в ней необходимые поля:
    name - текстовое поле, максимальная длина 100 символов,создаём индекс и удобочитаемое имя
    image - строка, предоставляющая данные об изображении,
            создаём удобочитаемое имя и указываем путь хранения изображения
    description - текстовое поле неограниченной длины и необязательное к заполнению,
                создаём удобочитаемое имя
    prise - поле для хранения десятичного числа с фиксированной точностью,
            указываем общее количество цифр, допустимых в числе и колличество цифр после точки,
            а также удобочитаемое имя
Также модель имеет стандартный метод класса __str__(), чтобы вернуть удобочитаемую строку для объекта
"""


from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наменование')
    image = models.ImageField(verbose_name='Изображение', upload_to='products/')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
