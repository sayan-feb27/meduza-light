from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from .views import NewsListView

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    path(
        "schema",
        get_schema_view(
            title="Meduza Light",
            description="News API",
            version="1.0.0",
            urlconf="news.api.v1.urls",
        ),
        name="openapi-schema",
    ),
    path("news/", NewsListView.as_view()),
]
