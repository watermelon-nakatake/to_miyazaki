from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import RestaurantImage, MenuImage, Restaurant, RestaurantMenu, Genre, CityName, CityArea
from django.views import generic
from .forms import PostCreateForm


def index(request):
    """
    インデックスページ(Topページ)を表示
    """
    return HttpResponse("Hello, world. You are in info_edit index.")


def menu_detail(request, menu_id):
    """
    メニューページを表示
    """
    return HttpResponse("You're looking at question %s." % menu_id)


def restaurant_detail(request, restaurant_id):
    """
    検索結果からの店の情報ページを表示
    """
    this_restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_list = get_list_or_404(RestaurantMenu, sub_restaurant=this_restaurant)
    view_menu_list = [{'name_text': menu.menu_name_text, 'price': menu.menu_price,
                       'comment_text': menu.menu_comment_text,
                       'images': MenuImage.objects.filter(sub_menu=menu)} for menu in menu_list]
    print(view_menu_list)
    restaurant_images = get_list_or_404(RestaurantImage, sub_restaurant=this_restaurant)
    return render(request, 'info_edit/detail.html', {'this_restaurant': this_restaurant,

                                                     'menu_list': view_menu_list, 'image_list': restaurant_images})


def edit_main_info(request, restaurant_id):
    """
    店が店舗情報をインプットする画面を表示
    """
    restaurant = get_list_or_404(Restaurant, pk=restaurant_id)
    genre_list = Genre.objects.all()
    city_list = CityName.objects.all()
    form_class = PostCreateForm
    return render(request, 'info_edit/main_info.html', {'restaurant_id': restaurant_id, 'genre_list': genre_list,
                                                        'city_list': city_list, 'form_class': form_class})





