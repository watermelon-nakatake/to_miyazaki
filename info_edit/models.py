from django.db import models
import os
from stdimage.models import StdImageField
from django import forms
from register.models import User
from django.conf import settings


class RestaurantStaff(models.Model):
    user = models


class CityName(models.Model):
    city_name_text = models.CharField('市区町村', max_length=10)

    def __str__(self):
        return self.city_name_text


class CityArea(models.Model):
    city_name = models.ForeignKey(CityName, on_delete=models.CASCADE)
    area_name_text = models.CharField(max_length=10)

    def __str__(self):
        return self.area_name_text


class Genre(models.Model):
    genre_text = models.CharField(max_length=10)

    def __str__(self):
        return self.genre_text


class Restaurant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    restaurant_name_text = models.CharField('店名', max_length=20)
    pub_date = models.DateTimeField('作成日時', auto_now_add=True)
    mod_date = models.DateTimeField('更新日時', auto_now=True)
    restaurant_address = models.CharField('所在地', max_length=200)
    restaurant_city = models.ForeignKey(CityName, on_delete=models.CASCADE, verbose_name='市区町村')
    city_area = models.ManyToManyField(CityArea, verbose_name='エリア')
    restaurant_genre = models.ManyToManyField(Genre, verbose_name='ジャンル')
    restaurant_comment = models.CharField('コメント', max_length=300, blank=True)
    image_num = models.IntegerField(default=0)

    def __str__(self):
        return self.restaurant_name_text


class RestaurantMenu(models.Model):
    sub_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name_text = models.CharField('料理名', max_length=100)
    menu_comment_text = models.CharField('コメント', max_length=300)
    menu_price = models.IntegerField('価格', default=0, blank=True)
    image_num = models.IntegerField(default=0)

    def __str__(self):
        return self.menu_name_text


def make_upload_path(instance, file_name):
    prefix = 'images/'
    user_id = instance.sub_restaurant.pk
    image_num = instance.sub_restaurant.image_num
    ext = os.path.splitext(file_name)[-1]
    return '{}r{}_{}{}'.format(prefix, str(user_id).zfill(5), str(image_num).zfill(3), ext)


def make_menu_upload_path(instance, file_name):
    prefix = 'images/'
    user_id = instance.sub_menu.pk
    image_num = instance.sub_menu.image_num
    ext = os.path.splitext(file_name)[-1]
    return '{}m{}_{}{}'.format(prefix, str(user_id).zfill(5), str(image_num).zfill(3), ext)


class RestaurantImage(models.Model):
    image = StdImageField(upload_to=make_upload_path, blank=True, null=True,
                          variations={'large': (600, 400), 'thumbnail': (150, 100)})
    sub_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True)


class MenuImage(models.Model):
    image = StdImageField(upload_to=make_menu_upload_path, blank=True, null=True,
                          variations={'large': (600, 400), 'thumbnail': (150, 100)})
    sub_menu = models.ForeignKey(RestaurantMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True)


class RestaurantImageForm(forms.ModelForm):
    class Meta:
        models = RestaurantImage
        fields = ['image', 'title', 'sub_restaurant']
