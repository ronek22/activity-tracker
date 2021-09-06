# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from activity.models import Activity


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)


class ActivityDetailView(LoginRequiredMixin, DetailView):
    model = Activity


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    fields = ["type", "effort", "name", "description", "distance", "duration"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActivityUpdateView(LoginRequiredMixin, UpdateView):
    model = Activity
    fields = ["type", "effort", "name", "description", "distance", "duration"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("activity:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    model = Activity
    success_url = reverse_lazy('activity:list')
