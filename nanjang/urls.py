from django.urls import path
from . import views

app_name = 'nanjang'

urlpatterns = [
    
    # GET '/nanjang/99/
    path('<int:pk>/', views.NanjangDetailView.as_view(), name='detail'),

    # POST '/nanjang/like/99/
    path('like/<int:pk>/', views.nanjang_like, name='like')
]
