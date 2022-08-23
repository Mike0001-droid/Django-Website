from django.contrib import admin
from django.urls import path
from Application import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('blog/<slug:slug>', views.article_page, name='article_page'),
]
