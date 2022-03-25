from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from women.views import pageNotFound
from coolsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound