from django.db import models
import re
from PIL import Image
import os
from stdimage.models import StdImageField

"""
class OriginalRImages(models.Model):
    image = models.ImageField(upload_to='original_images/', blank=True, null=True)

    def __str__(self):
        image_path = re.sub(r'^.*original_images/', '', self.image.path)
        return image_path

    def resize_image(self, restaurant_id, size):
        img = Image.open(self.image.path)
        image_resize = img.resize(size, Image.LANCZOS)
        this_restaurant = Restaurant.objects.get(pk=restaurant_id)
        image_num = this_restaurant.image_num
        image_path = '../images/r{}_{}{}'.format(str(restaurant_id).zfill(5), str(image_num + 1).zfill(3),
                                                 os.path.splitext(self.image.path)[1])
        image_resize.save(image_path)
        return image_path.replace('../', '')


class OriginalMImages(models.Model):
    image = models.ImageField(upload_to='original_images/', blank=True, null=True)

    def __str__(self):
        image_path = re.sub(r'^.*original_images/', '', self.image.path)
        return image_path

    def resize_image(self, menu_id, size):
        img = Image.open(self.image.path)
        image_resize = img.resize(size, Image.LANCZOS)
        this_menu = RestaurantMenu.objects.get(pk=menu_id)
        image_num = this_menu.image_num
        image_path = '../images/m{}_{}{}'.format(str(menu_id).zfill(5), str(image_num + 1).zfill(3),
                                                 os.path.splitext(self.image.path)[1])
        image_resize.save(image_path)
        return image_path.replace('../', '')
"""


class CityName(models.Model):
    city_name_text = models.CharField(max_length=10)

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
    restaurant_name_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    mod_date = models.DateTimeField('date modified')
    restaurant_address = models.CharField(max_length=200)
    restaurant_city = models.ForeignKey(CityName, on_delete=models.CASCADE)
    city_area = models.ForeignKey(CityArea, on_delete=models.CASCADE)
    restaurant_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    restaurant_comment = models.CharField(max_length=300, blank=True)
    image_num = models.IntegerField(default=0)

    def __str__(self):
        return self.restaurant_name_text


class RestaurantMenu(models.Model):
    sub_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name_text = models.CharField(max_length=100)
    menu_comment_text = models.CharField(max_length=300)
    menu_price = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.menu_name_text


def make_upload_path(instance, file_name):
    prefix = '/images/'
    print(instance)
    print(file_name)
    user_id = instance.sub_restaurant.pk
    image_num = instance.sub_restaurant.image_num
    ext = os.path.splitext(file_name)[-1]
    return '{}r{}_{}{}'.format(prefix, str(user_id).zfill(5), str(image_num).zfill(3), ext)


class RestaurantImage(models.Model):
    image = StdImageField(upload_to=make_upload_path, blank=True, null=True,
                          variations={'large': (600, 400), 'thumbnail': (150, 100)})
    sub_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class MenuImage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    sub_menu = models.ForeignKey(RestaurantMenu, on_delete=models.CASCADE)
