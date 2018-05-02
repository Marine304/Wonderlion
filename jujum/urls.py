from django.urls import path
from . import views

app_name = 'jujum'

urlpatterns = [
    # GEt '/jujum/'
    
    # GET '/jujum/99/
    path('<int:pk>/', views.JujumDetailView.as_view(), name='detail'),
]
