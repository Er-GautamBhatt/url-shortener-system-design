import requests
from .models import ClickEvent
from user_agents import parse


IPINFO_TOKEN = "1dd24d45651615"

def get_country(ip):
    try:
        response = requests.get(
            f"https://api.ipinfo.io/lite/{ip}",
            headers={
                "Authorization": f"Bearer {IPINFO_TOKEN}"
            },
            timeout=3
        )

        response.raise_for_status()

        data = response.json()

        return data.get("country_code", "")

    except Exception:
        return ""


def parse_user_agent(user_agent):

    ua = parse(user_agent)

    if ua.is_mobile:
        device = "Mobile"

    elif ua.is_tablet:
        device = "Tablet"

    elif ua.is_pc:
        device = "Desktop"

    else:
        device = "Unknown"

    return {
        "browser": ua.browser.family,
        "os": ua.os.family,
        "device": device,
    }

def track_click(request, short_code):

    ip = get_client_ip(request)

    user_agent = request.META.get(
        "HTTP_USER_AGENT",
        ""
    )

    referrer = request.META.get(
        "HTTP_REFERER",
        ""
    )

    parsed = parse_user_agent(
        user_agent
    )

    ClickEvent.objects.create(
        short_code=short_code,
        ip_address=ip,
        country=get_country(ip),
        browser=parsed["browser"],
        operating_system=parsed["os"],
        device_type=parsed["device"],
        referrer=referrer,
        user_agent=user_agent,
    )

def get_client_ip(request):

    x_forwarded_for = request.META.get(
        "HTTP_X_FORWARDED_FOR"
    )

    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]

    return request.META.get(
        "REMOTE_ADDR"
    )