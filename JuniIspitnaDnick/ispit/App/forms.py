from django import forms
from .models import Product, Kategorija


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("user", )
        fields = ['ime', 'opis', 'photo', 'cena', 'kolicina', 'kategorija']

