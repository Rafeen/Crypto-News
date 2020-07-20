from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, PriceView

app_name = 'crypto'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("prices/", PriceView.as_view(), name='prices'),
]
