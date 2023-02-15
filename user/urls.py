from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CreateUserView, ManageUserView, EmailTokenObtainPairView

app_name = "account"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", ManageUserView.as_view(), name="me"),
]
