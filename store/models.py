from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL, CASCADE, PROTECT


class Territory(models.Model):
    territory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.territory_name


class Trade(models.Model):
    trade_name = models.CharField(max_length=255)

    def __str__(self):
        return self.trade_name


class Details(models.Model):
    user = models.ForeignKey(
        User, default=None, on_delete=CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


a = '10%'
b = '20%'
c = '30%'
d = '40%'
e = '50%'
f = '60%'
g = '70%'
h = '80%'
i = '90%'
j = '100%'
Percents = [
    (a, '10%'), (b, '20%'), (c, '30%'),
    (d, '40%'), (e, '50%'), (f, '60%'),
    (g, '70%'), (h, '80%'), (i, '90%'), (j, '100%')
]


class United(models.Model):
    detail = models.ForeignKey(Details, CASCADE, blank=True, null=True)
    percent = models.CharField(max_length=20, choices=Percents, null=True)

    def __str__(self):
        return f'{self.detail} {self.percent}'


class Sku(models.Model):
    img = models.FileField(upload_to='media/%y/%m/%d/',
                           default='default.png', blank=True)
    sku_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.sku_name}'


class Visit(models.Model):
    territory = models.ForeignKey(
        Territory, on_delete=models.CASCADE, null=True, related_name='Территория')
    trade = models.ForeignKey(
        Trade, on_delete=models.CASCADE, related_name='Магазин')
    sku = models.ManyToManyField(Sku, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    united = models.ManyToManyField(United, blank=True)
    detail = models.ManyToManyField(Details, blank=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.trade} {self.visit_date}'
