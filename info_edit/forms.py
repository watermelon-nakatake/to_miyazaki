from .models import Restaurant, CityName, CityArea
from django import forms


class MakeRestaurantMain(forms.ModelForm):
    parent_category = forms.ModelChoiceField(label='city_name', queryset=CityName.objects, required=False)

    class Meta:
        model = Restaurant
        fields = '__all__'
