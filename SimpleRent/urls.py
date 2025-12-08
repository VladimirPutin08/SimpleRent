from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

from django.urls import path, include

urlpatterns = [
    path("api/accounts/", include("accounts.urls")),
]
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def index(request):
    return JsonResponse({"status": "ok", "message": "SimpleRent API is online 🚀"})

urlpatterns = [
    path("", index),                        # 👈 returns JSON
    path("api/accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # existing register/login endpoints if you have them
]
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def index(request):
    return JsonResponse({"status":"ok", "message":"SimpleRent API is online 🚀"})

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),   # <--- this line must point to accounts.urls
]
