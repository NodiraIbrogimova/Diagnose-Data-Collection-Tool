from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from src.core.swagger import urlpatterns as doc_urls

urlpatterns = doc_urls


urlpatterns += [
    path("admin/", admin.site.urls),
    path("v1/account/", include("src.account.urls"), name="account"),
    path("v1/", include("src.diagnose.urls"), name="diagnose"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
