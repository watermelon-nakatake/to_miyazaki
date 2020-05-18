from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('<int:restaurant_id>/<int:menu_id>/', views.menu_detail, name='menu_detail'),
]
