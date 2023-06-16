from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path('vols/', include('vols.urls')),
    path('my_hotel/', include('my_hotel.urls')),
    path('reservation/', include('reservation.urls')),
    path('location_voiture/', include('location_voiture.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
