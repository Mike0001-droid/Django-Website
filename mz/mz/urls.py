from django.contrib import admin
from Application import views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('blog/<slug:slug>', views.article_page, name='article_page'),
    path('', include('Application.urls')),
]
