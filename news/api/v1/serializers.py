from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    date = serializers.CharField(source="published")
    subject = serializers.CharField(source="title")
    content = serializers.CharField(source="body")

    class Meta:
        model = News
        fields = ["date", "subject", "content"]
