from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from api.urls import urlpatterns as api_urls
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls))
]

urlpatterns += (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
