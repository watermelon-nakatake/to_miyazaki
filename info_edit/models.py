from django.db import models


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

    def __str__(self):
        return self.restaurant_name_text


class RestaurantMenu(models.Model):
    sub_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name_text = models.CharField(max_length=100)
    menu_comment_text = models.CharField(max_length=300)
    menu_price = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.menu_name_text
