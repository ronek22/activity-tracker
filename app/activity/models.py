from decimal import Decimal

from django.conf import settings
from django.db import models


# Create your models here.
from django.urls import reverse


class Activity(models.Model):
    class Types(models.TextChoices):
        RUNNING = "Running"
        CYCLING = "Cycling"
        HIKING = "Hiking"

    class Effort(models.TextChoices):
        EASY = "Easy"
        MODERATE = "Moderate"
        MAX_EFFORT = "Max Effort"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    type = models.CharField(
        max_length=7,
        choices=Types.choices,
        default=Types.RUNNING,
        verbose_name="Activity Type"
    )
    effort = models.CharField(
        max_length=20,
        choices=Effort.choices,
        default=Effort.EASY,
        verbose_name="Activity Effort"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400, null=True, blank=True)
    duration = models.DurationField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField("created_at", db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", db_index=True, auto_now=True)

    def _speed(self) -> str:
        seconds = Decimal(self.duration.total_seconds())
        speed = self.distance / (seconds/3600)
        return f"{speed:.2f}"

    def _pace(self) -> str:
        seconds = Decimal(self.duration.total_seconds())
        seconds_per_km = seconds / self.distance
        minutes_per_km = seconds_per_km // 60
        seconds_remainder = int(seconds_per_km - (minutes_per_km * 60))
        return f"{minutes_per_km}:{seconds_remainder:0=2d}"

    @property
    def speed(self) -> str:
        if self.type == self.Types.CYCLING:
            return self._speed()
        return self._pace()

    def get_absolute_url(self):
        return reverse("activity:detail", args=[str(self.id)])

    def __str__(self) -> str:
        return f"{self.name} | {self.distance} km | {self.duration}"

    class Meta:
        db_table = "activities"
        verbose_name_plural = "Activities"
