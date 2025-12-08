from django.urls import path
from .views import RegisterUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),   # <-- Missing earlier
    path('api/', include('accounts.jwt_urls')),        # or wherever your token urls are
]
