from django.urls import path

from authentication.views import LoginView, LogoutView, SignUpView

app_name = "authentication"

urlpatterns = [
    path("register", SignUpView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout")
]