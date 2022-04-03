
from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('kawage.apps.public.urls')),
    path("accounts/", include('kawage.apps.accounts.urls')),
         # django auth
    path(
        "accounts/login",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
]
