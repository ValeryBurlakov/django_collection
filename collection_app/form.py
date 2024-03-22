from django import forms

from .models import Coin, Collection


class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ['name', 'description', 'value', 'condition', 'photo_obverse', 'photo_reverse', 'collection']


class GetCoinForm(forms.ModelForm):
    id = forms.IntegerField()  # добавляем поле id в форме

    class Meta:
        model = Coin
        fields = ['id']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name']
