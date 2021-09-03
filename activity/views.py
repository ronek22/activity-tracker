# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from activity.models import Activity


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity


class ActivityDetailView(LoginRequiredMixin, DetailView):
    model = Activity


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    fields = ["type", "effort", "name", "description", "distance", "duration"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
