
from django.contrib import admin
from django.urls import include, path
from config.settings import django
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("learning_views.urls")),
] + static(django.MEDIA_URL, document_root=django.MEDIA_ROOT)

urlpatterns += static(django.STATIC_URL, document_root=django.STATIC_ROOT)
