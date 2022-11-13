from django.urls import path

from knox import views as knox_views

from accounts.views import LoginView

from .views import RegistrationView


urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("logoutAll/", knox_views.LogoutAllView.as_view(), name="logout_all"),
]
