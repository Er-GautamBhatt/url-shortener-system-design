from django.db import models


class ShortURL(models.Model):
    original_url = models.URLField(max_length=2048)

    short_code = models.CharField(
        max_length=10,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True
    )

    click_count = models.PositiveBigIntegerField(
        default=0
    )

    def __str__(self):
        return self.short_code