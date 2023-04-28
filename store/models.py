from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL, CASCADE, PROTECT


class Sku(models.Model):
    user = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='media/%y/%m/%d/',
                             default='default.png', null=True, blank=True)
    sku_name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.sku_name


class Territory(models.Model):
    territory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.territory_name


class Trade(models.Model):
    name_trade = models.CharField(max_length=255)

    def __str__(self):
        return self.name_trade


class Details(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class United(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=CASCADE, null=True, blank=True)
    name_detail = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.name_detail}'


class Visit(models.Model):
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    sku = models.ManyToManyField(Sku, blank=True)
    trade = models.ForeignKey(Trade, SET_NULL, null=True)
    territory = models.ForeignKey(Territory, SET_NULL, null=True)
    detail = models.ManyToManyField(Details, blank=True)
    united = models.ManyToManyField(United, blank=True)
    comment = models.TextField(blank=True, null=True, )

    def __str__(self):
        return f'{self.user} in {self.date}'
