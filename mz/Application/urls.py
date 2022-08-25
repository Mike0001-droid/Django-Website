from django.urls import path, include
from .views import courses

urlpatterns = [
    path('courses/', courses.as_view(), name='courses'),
]