from django.contrib import admin
from django.urls import path, include
from .api import api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
    path('sistemas/', include('Sistemas.urls')),
    path('api/', api.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
