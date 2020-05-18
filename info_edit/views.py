from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Restaurant, RestaurantMenu


def index(request):
    return HttpResponse("Hello, world. You are in info_edit index.")


def menu_detail(request, menu_id):
    return HttpResponse("You're looking at question %s." % menu_id)


def restaurant_detail(request, restaurant_id):
    this_restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_list = get_list_or_404(RestaurantMenu, sub_restaurant=this_restaurant)
    return render(request, 'info_edit/detail.html', {'this_restaurant': this_restaurant,
                                                     'menu_list': menu_list})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
