from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import RestaurantImage, MenuImage, Restaurant, RestaurantMenu, Genre, CityName, CityArea
from .forms import MakeRestaurantMain
from django.contrib.auth.decorators import login_required
from django.contrib.auth.base_user import AbstractBaseUser


def index(request):
    """
    インデックスページ(Topページ)を表示
    """
    if AbstractBaseUser.is_authenticated:
        user = AbstractBaseUser
        restaurant_id = Restaurant.objects
    else:
        user = None
        restaurant_id = None
    return render(request, 'info_edit/top.html', {'user': user, 'restaurant_id': restaurant_id})


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
    return render(request, 'info_edit/detail.html', {'this_restaurant': this_restaurant, 'menu_list': view_menu_list,
                                                     'image_list': restaurant_images})


@login_required
def edit_main_info(request, restaurant_id):
    """
    店が店舗情報をインプットする画面を表示
    """
    restaurant = get_list_or_404(Restaurant, pk=restaurant_id)
    form_class = (request.GET or None)
    if form_class.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    context = {'restaurant_id': restaurant_id, 'form': form_class, 'message': message}
    return render(request, 'info_edit/edit_main_info.html', context)


@login_required
def make_main_info(request):
    """
    店が店舗情報を最初にインプットする画面を表示
    """
    form_class = MakeRestaurantMain(request.GET or None)
    if form_class.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    context = {'form': form_class, 'message': message}
    return render(request, 'info_edit/make_main_info.html', context)


