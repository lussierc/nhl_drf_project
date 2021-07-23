"""Defines the different views for APIs."""

from django.shortcuts import render
from rest_framework import generics, permissions

from .models import TeamInfo
from .serializers import TeamInfoSerializer

# Create your views here.


class TeamInfoList(generics.ListCreateAPIView):
    """
    A list/table of hockey team information. With this, new teams can be added to the API list & they can also be viewed.
    """

    queryset = TeamInfo.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]  # public api you can browse, but must be authenticated to change things
    serializer_class = TeamInfoSerializer


class TeamInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Handle requests to individual teams in the API List view. Requests can include retrieve requests (GET), update, and deletion requests for individual teams in the table.
    """

    queryset = TeamInfo.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]  # public api you can browse, but must be authenticated to change things
    serializer_class = TeamInfoSerializer
