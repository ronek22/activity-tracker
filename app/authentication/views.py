from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout as auth_logout
from authentication.forms import NewUserForm


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "auth/register.html"
    success_url = reverse_lazy("authentication:login")
    form_class = NewUserForm
    success_message = "Your profile was created successfully"


class LoginView(auth_views.LoginView):
    template_name = "auth/login.html"
    form_class = auth_views.AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('activity:list')


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy("authentication:login")

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)