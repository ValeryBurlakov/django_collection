from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='Имя')
    registration_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name


class Coin(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='Описание')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='номинал')
    added_date = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    photo = models.ImageField(upload_to='collection_app/coin_photos/', null=True, blank=True,
                              default='collection_app/coin_photos/default_image.jpg')

    def __str__(self):
        return f'{self.name}'


class Collection(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    coins = models.ManyToManyField(Coin, verbose_name='Монеты')

    def __str__(self):
        return f'{self.user}'
