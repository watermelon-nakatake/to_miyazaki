from .models import Restaurant, CityName, CityArea
from django import forms
from register.models import User


class MakeRestaurantMain(forms.ModelForm):
    parent_category = forms.ModelChoiceField(label='city_name', queryset=CityName.objects, required=False)

    class Meta:
        model = Restaurant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget['class'] = 'form-control'


class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = Restaurant
        exclude = ('user_account', 'pub_date', 'mod_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class UserCreateForm(forms.ModelForm):
    """レストラン情報新規作成フォーム"""

    class Meta:
        model = Restaurant
        exclude = ('user_account', 'pub_date', 'mod_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
