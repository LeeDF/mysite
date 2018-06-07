from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/<str:pwd>/login/', views.login, name='login'),
]
