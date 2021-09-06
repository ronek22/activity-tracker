from django.urls import path

from activity.views import ActivityCreateView, ActivityDeleteView, ActivityDetailView, ActivityListView, ActivityUpdateView

app_name = "activity"

urlpatterns = [
    path("", ActivityListView.as_view(), name="list"),
    path("<int:pk>", ActivityDetailView.as_view(), name="detail"),
    path("<int:pk>/update", ActivityUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", ActivityDeleteView.as_view(), name="delete"),
    path("create", ActivityCreateView.as_view(), name="create")
]