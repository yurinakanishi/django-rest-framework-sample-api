from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from accounts.views import Registration, UserInfo, Logout

urlpatterns = [
    path("register/", Registration.as_view(), name="register"),
    path("user/", UserInfo.as_view(), name="user"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
