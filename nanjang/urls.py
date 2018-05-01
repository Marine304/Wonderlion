from django.urls import path
from . import views

app_name = 'nanjang'

urlpatterns = [
    
    # GET '/nanjang/
    path('', views.NanjangListView.as_view(), name='list'),
    # GET '/nanjang/99/
    path('<int:pk>/', views.NanjangDetailView.as_view(), name='detail'),
]
