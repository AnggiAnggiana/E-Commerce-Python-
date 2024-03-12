from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stores.urls')),
    path('auth_user/', include('django.contrib.auth.urls')),
    path('auth_user/', include('auth_user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
