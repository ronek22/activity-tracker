from django.urls import path

from activity.views import ActivityCreateView, ActivityDetailView, ActivityListView

app_name = "activity"

urlpatterns = [
    path("", ActivityListView.as_view(), name="list"),
    path("<int:pk>", ActivityDetailView.as_view(), name="detail"),
    path("create", ActivityCreateView.as_view(), name="create")
]