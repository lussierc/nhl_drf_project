"""Defines URL paths for teams API, including overall API list and individual team details."""

from django.urls import path

from . import views

urlpatterns = [
    path("teams/", views.TeamInfoList.as_view()),
    path("teams/<int:pk>/", views.TeamInfoDetails.as_view()),
]
