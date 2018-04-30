from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # GET 'home/'
    path('', views.IndexView.as_view(), name='index'),

    # GET 'home/main/'
    # path('main/', views.main, name='main'),
    path('main/', views.MainView.as_view(), name='main'),

    # GET 'home/main/jujum/99/
    path('main/jujum/<int:pk>/', views.JujumDetailView.as_view(), name='main-jujum'),

    # GET 'home/main/nanjang/99/
    path('main/nanjang/<int:pk>/', views.NanjangDetailView.as_view(), name='main-nanjang'),
]
