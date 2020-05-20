from .models import Restaurant, CityName, CityArea
from django import forms


class PostCreateForm(forms.ModelForm):
    parent_category = forms.ModelChoiceField(label='city_name', queryset=CityName, required=False)

    class Meta:
        model = Restaurant
        fields = '__all__'

