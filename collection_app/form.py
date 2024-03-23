from django import forms

from .models import Coin, Collection, Country


class CoinForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CoinForm, self).__init__(*args, **kwargs)
        self.fields['collection'].queryset = Collection.objects.filter(user=user)
        # self.fields['country'].queryset = Country.objects.all()
        self.fields['country'].queryset = Country.objects.order_by('name')
    class Meta:
        model = Coin
        fields = ['name', 'description', 'value', 'condition', 'country', 'photo_obverse', 'photo_reverse', 'collection']


class GetCoinForm(forms.ModelForm):
    id = forms.IntegerField()  # добавляем поле id в форме

    class Meta:
        model = Coin
        fields = ['id']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name']
