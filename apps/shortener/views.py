from django.shortcuts import redirect
from django.http import Http404

from .models import ShortURL

from apps.analytics.services import (
    track_click
)


def redirect_url(request, code):

    try:

        short_url = ShortURL.objects.get(
            short_code=code
        )

    except ShortURL.DoesNotExist:

        raise Http404()

    short_url.click_count += 1

    short_url.save(
        update_fields=["click_count"]
    )

    track_click(
        request,
        code
    )

    return redirect(
        short_url.original_url
    )