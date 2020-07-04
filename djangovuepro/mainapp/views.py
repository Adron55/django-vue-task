from django.shortcuts import render

# Create your views here.
from .models import News
from .serializers import NewsSerializer
from rest_framework import generics


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer