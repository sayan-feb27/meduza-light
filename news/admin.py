from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ("title", "slug", "published")
    search_fields = ("title", "slug")
    date_hierarchy = "published"
    list_filter = ("is_archived",)


admin.site.register(News, NewsAdmin)
