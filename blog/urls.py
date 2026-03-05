from django.urls import path
from . import views

urlpatterns = [
    # 页面路由
    path('', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),

    # API路由
    path('api/articles/', views.api_article_list, name='api_article_list'),
    path('api/articles/<int:pk>/', views.api_article_detail, name='api_article_detail'),
    path('api/articles/create/', views.api_article_create, name='api_article_create'),
]