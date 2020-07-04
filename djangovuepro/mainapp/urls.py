from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mainapp import views

urlpatterns = [
    path('news/', views.NewsList.as_view()),
    path('news/<int:pk>/', views.NewsDetail.as_view()),
]