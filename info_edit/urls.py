from django.urls import path

from . import views

app_name = 'info_edit'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/make_main/', views.make_main_info, name='make_main_info'),
    path('user/edit_main/<int:restaurant_id>/', views.edit_main_info, name='edit_main_info'),
    # path('user/make_menu/', views.edit_main_info, name='edit_main_info'),
    # path('user/edit_menu/<int:restaurant_id>/', views.edit_main_info, name='edit_main_info'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/<int:menu_id>/', views.menu_detail, name='menu_detail'),
]
