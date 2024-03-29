from django.contrib import admin
from django.urls import path, include
from main import urls as main_path_urls
from django.conf.urls.static import static
from django.conf import settings
from users import urls as user_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_path_urls)),
    path('', include(user_app_urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
