from django.urls import path

from .views import ShortenAPIView, AnalyticsAPIView

urlpatterns = [
    path(
        "shorten/",
        ShortenAPIView.as_view()
    ),
    path(
        "analytics/<str:code>/",
        AnalyticsAPIView.as_view()
    ),
]