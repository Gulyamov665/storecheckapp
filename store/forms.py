from django import forms
from django.contrib.auth.models import User

from store.models import *


class VisitForm(forms.ModelForm):
    trade = forms.Select()
    territory = forms.Select()
    sku = forms.ChoiceField(required=False)
    detail = forms.ChoiceField(required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Comment')

    class Meta:
        model = Visit
        fields = ['trade', 'territory', 'sku', 'detail', 'comment']


class TerritoryForm(forms.ModelForm):
    territory_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Name of Territory')

    class Meta:
        model = Territory
        fields = ['territory_name']


class TradeForm(forms.ModelForm):
    name_trade = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Name of Trade')

    class Meta:
        model = Trade
        fields = ['name_trade']


class SkuForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control'}), label='Image', required=False)
    sku_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Name of SKU')

    class Meta:
        model = Sku
        fields = ['image', 'sku_name']


class UnitedForm(forms.ModelForm):
    name_detail = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Other')

    class Meta:
        model = United
        fields = ['name_detail']

class DetailForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Other details')

    class Meta:
        model = Details
        fields = ['name']
