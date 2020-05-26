from django.urls import path

from . import views

app_name = 'info_edit'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/top', views.Top.as_view(), name='user_top'),
    path('user/create_main/<int:pk>', views.UserCreate.as_view(), name='user_create'),
    path('user/detail_main/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('user/edit_main/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    # path('user/make_menu/', views.edit_main_info, name='edit_main_info'),
    # path('user/edit_menu/', views.edit_main_info, name='edit_main_info'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/<int:menu_id>/', views.menu_detail, name='menu_detail'),
]
