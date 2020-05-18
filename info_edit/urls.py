from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:restaurant_id>/', views.main_info, name='main_info'),
    path('<int:restaurant_id>/<int:menu_id>/', views.menu_detail, name='menu_detail'),
]
