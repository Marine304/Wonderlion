from django.urls import path
from . import views

app_name = 'jujum'

urlpatterns = [
    # GET '/jujum/99/
    path('<int:pk>/', views.JujumDetailView.as_view(), name='detail'),
    path('like/<int:pk>/', views.jujum_like, name='like')
]
