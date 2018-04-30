from django.urls import include, path
from django.contrib import admin
from home.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    path('home/', include('home.urls', namespace="home")),
    path('admin/', admin.site.urls),
]