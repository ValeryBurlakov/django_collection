from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     username = models.CharField(max_length=100, verbose_name='Имя')
#     password = models.CharField(max_length=128, editable=False)
#     registration_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
#
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
#
#     def __str__(self):
#         return self.username


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название страны')

    def __str__(self):
        return self.name


class CoinState(models.Model):
    name = models.CharField(max_length=100, verbose_name='Состояние')

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Coin(models.Model):
    # CONDITION_CHOICES = [
    #     ('Плохое', 'Плохое'),
    #     ('Среднее', 'Среднее'),
    #     ('Отличное', 'Отличное'),
    #     ('Не определено', 'Не определено'),
    # ]
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Коллекция', null=True, blank=True, default=None)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='Описание')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='номинал')
    year_coin = models.IntegerField(verbose_name='Год', null=True, blank=True, default=None)
    # condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, verbose_name='Состояние', default='Не определено')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна', null=True, blank=True,
                                default=None)
    coinstate = models.ForeignKey(CoinState, on_delete=models.CASCADE, verbose_name='состояние', null=True, blank=True,
                                default=None)
    added_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    photo_obverse = models.ImageField(upload_to='collection_app/coin_photos/', null=True, blank=True,
                              default='collection_app/coin_photos/default_image.jpg', verbose_name='фото аверс')
    photo_reverse = models.ImageField(upload_to='collection_app/coin_photos/', null=True, blank=True,
                                      default='collection_app/coin_photos/default_image.jpg', verbose_name='фото реверс')
    price = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='примерная стоимость', null=True, blank=True,
                                default=None)
    def __str__(self):
        return f'{self.name}'
