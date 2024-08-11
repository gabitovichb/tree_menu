from django.urls import path

from .views import BaseTemplateView


urlpatterns = [
    path("", BaseTemplateView.as_view(), name="base"),
    path("url/<url>/", BaseTemplateView.as_view(), name="item"),
]
