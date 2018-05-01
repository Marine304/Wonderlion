from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # GET 'home/'
    path('', views.IndexView.as_view(), name='index'),
    # GET 'home/main/'
    # path('main/', views.main, name='main'),
    path('main/', views.MainView.as_view(), name='main')
]
