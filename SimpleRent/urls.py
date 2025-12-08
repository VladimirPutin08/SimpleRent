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
