from django.db import models


class ClickEvent(models.Model):

    short_code = models.CharField(
        max_length=20,
        db_index=True
    )

    ip_address = models.GenericIPAddressField()

    country = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    browser = models.CharField(
        max_length=100,
        blank=True
    )

    operating_system = models.CharField(
        max_length=100,
        blank=True
    )

    device_type = models.CharField(
        max_length=50,
        blank=True
    )

    referrer = models.TextField(
        blank=True
    )

    user_agent = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]