from django.urls import path
from . import views

urlpatterns = [
    # GET 'home/'
    path('', views.IndexView.as_view(), name='index'),

    # GET 'home/main/'
    path('main/', views.MainView.as_view(), name='main'),
    
    # GET 'home/nanjang'
    path('nanjang/', views.NanjangListView.as_view(), name='nanjang'),
    
]
