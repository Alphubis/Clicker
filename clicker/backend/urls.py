from django.urls import path
from backend import views


boosts_list = views.BoostViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

boosts_details = views.BoostViewSet.as_view({
    'put': 'update',
})

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('call_click/', views.call_click, name='call_click'),
    path('boosts/', boosts_list, name='boosts'),
    path('boosts/<int:pk>', boosts_details, name='boosts'),
]
