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
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class PercentItem(models.Model):
    name_per = models.CharField(max_length=50)

    def __str__(self):
        return self.name_per


a = '0%'
b = '10%'
c = '20%'
d = '30%'
e = '40%'
f = '50%'
g = '60%'
h = '70%'
i = '80%'
j = '90%'
k = '100%'
Percents = [
    (a, '0%'), (b, '10%'), (c, '20%'),
    (d, '30%'), (e, '40%'), (f, '50%'),
    (g, '60%'), (h, '70%'), (i, '80%'), (j, '90%'), (k, '100%')
]


class United(models.Model):
    percent = models.CharField(max_length=20, choices=Percents, null=True)

    def __str__(self):
        return f'{self.percent}'


class Sku(models.Model):
    img = models.FileField(upload_to='media/%y/%m/%d/', default='default.png', blank=True)
    sku_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.sku_name}'


class Visit(models.Model):
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE, null=True, related_name='Территория')
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name='Магазин')
    sku = models.ManyToManyField(Sku, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Coffee = models.CharField(max_length=20, choices=Percents, null=True)
    IN = models.CharField(max_length=20, choices=Percents, null=True)
    Tablets = models.CharField(max_length=20, choices=Percents, null=True)
    Countlines = models.CharField(max_length=20, choices=Percents, null=True)
    detail = models.ManyToManyField(Details, blank=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateField(auto_now=True, null=True)


    def __str__(self):
        return f'{self.trade} {self.visit_date}'
