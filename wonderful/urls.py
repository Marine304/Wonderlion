from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from home.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    path('home/', include('home.urls', namespace="home")),
    path('nanjang/', include('nanjang.urls', namespace="nanjang")),
    path('jujum/', include('jujum.urls', namespace="jujum")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
