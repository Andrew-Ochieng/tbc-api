from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('articles/', views.ArticleListAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', views.ArticleDetailAPIView.as_view(), name='article-detail'),
    # path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
]



