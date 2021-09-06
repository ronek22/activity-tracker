from django.contrib import admin

from activity.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "distance",
        "duration",
        "speed",
    )

    list_filter = ("user", "created_at", "updated_at")