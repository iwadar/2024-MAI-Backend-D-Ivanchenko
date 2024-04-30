from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
    name = models.CharField(max_length=30, blank=False)
    secondName = models.CharField(max_length=35, blank=False)
    phone = models.CharField(max_length=20, blank=False)

    def __str__(self) -> str:
        return f'{self.name} {self.secondName}'


class Cheese(models.Model):
    vendor_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=False)
    price = models.IntegerField(default=0, help_text='Цена за 1 кг')
    left = models.FloatField(default=1, help_text='Количество оставшегося сыра (кг)')
    description = models.TextField(help_text='Описание сыра', default='')

    def __str__(self) -> str:
        return f'Артикул: {self.vendor_code}, Название: {self.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Пользователь, оформивший заказ')
    data_order = models.DateField(blank=False)
    total = models.IntegerField(default=0, blank=False)
    list_cheeses = models.ManyToManyField(Cheese, through='List_cheese')

    def __str__(self) -> str:
        return f'№{self.id}, Заказчик: {self.user.name} {self.user.secondName}'


class List_cheese(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['order', 'cheese'], name='unique_position')] 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.1, blank=False)


    def __str__(self) -> str:
        return f'№{self.order.id}, Состав: {self.cheese.name}'
