from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import RestaurantImage, MenuImage, Restaurant, RestaurantMenu


def index(request):
    return HttpResponse("Hello, world. You are in info_edit index.")


def menu_detail(request, menu_id):
    return HttpResponse("You're looking at question %s." % menu_id)


def restaurant_detail(request, restaurant_id):
    this_restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_list = get_list_or_404(RestaurantMenu, sub_restaurant=this_restaurant)
    view_menu_list = [{'name_text': menu.menu_name_text, 'price': menu.menu_price,
                       'comment_text': menu.menu_comment_text,
                       'images': MenuImage.objects.filter(sub_menu=menu)} for menu in menu_list]
    restaurant_images = get_list_or_404(RestaurantImage, sub_restaurant=this_restaurant)
    return render(request, 'info_edit/detail.html', {'this_restaurant': this_restaurant,
                                                     'menu_list': view_menu_list, 'image_list': restaurant_images})
