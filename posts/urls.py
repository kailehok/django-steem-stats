# posts/urls.py
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('@<slug:account>/', HomePageView.as_view(), name='home')
]