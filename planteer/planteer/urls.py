from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  
    path('plants/', include('plants.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
