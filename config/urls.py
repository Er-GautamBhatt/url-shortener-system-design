from django.contrib import admin
from django.urls import path, include
from apps.shortener.views import (redirect_url)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls")),
    path("<str:code>/", redirect_url),
]