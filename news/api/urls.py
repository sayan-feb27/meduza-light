from django.urls import include, path

urlpatterns = [
    path("v1/", include("news.api.v1.urls")),
]
