from django.contrib import admin

from .models import Restaurant, RestaurantMenu, CityName, CityArea, Genre, RestaurantImage, MenuImage

admin.site.register(Restaurant)
admin.site.register(RestaurantMenu)
admin.site.register(CityName)
admin.site.register(CityArea)
admin.site.register(Genre)
admin.site.register(RestaurantImage)
admin.site.register(MenuImage)
