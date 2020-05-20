from django.urls import path

from . import views

app_name = 'info_edit'
urlpatterns = [
    path('', views.index, name='index'),
    path('account/<int:restaurant_id>/', views.edit_main_info, name='edit_main_info'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/<int:menu_id>/', views.menu_detail, name='menu_detail'),
]
