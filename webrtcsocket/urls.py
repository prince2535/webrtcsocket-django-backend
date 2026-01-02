from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path("api/", include("accounts.urls")),
    path("healthz", lambda r: HttpResponse("ok")),
]
