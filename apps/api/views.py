from rest_framework.views import APIView
from rest_framework.response import Response

from apps.shortener.services import (
    create_short_url
)
from apps.analytics.models import (
    ClickEvent
)


class ShortenAPIView(APIView):

    def post(self, request):

        original_url = request.data.get(
            "url"
        )

        short_url = create_short_url(
            original_url
        )

        return Response({
            "id": short_url.id,
            "short_code": short_url.short_code,
            "short_url": f"http://localhost:8000/{short_url.short_code}"
        })
    
class AnalyticsAPIView(APIView):

    def get(self, request, code):

        clicks = ClickEvent.objects.filter(
            short_code=code
        )

        return Response({

            "total_clicks": clicks.count(),

            "unique_visitors":
                clicks.values(
                    "ip_address"
                ).distinct().count(),

            "countries":
                list(
                    clicks.values(
                        "country"
                    )
                ),

            "devices":
                list(
                    clicks.values(
                        "device_type"
                    )
                ),

            "browsers":
                list(
                    clicks.values(
                        "browser"
                    )
                ),
        })
