from news.models import News
from rest_framework.generics import ListAPIView

from .serializers import NewsSerializer


class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
