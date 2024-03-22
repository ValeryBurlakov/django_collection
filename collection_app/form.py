from django import forms

from .models import Coin, Collection


class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ['name', 'description', 'value', 'photo']



class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'user', 'coins']
