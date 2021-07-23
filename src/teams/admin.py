"""Register models so they can be handled by the admin."""

from django.contrib import admin

from .models import TeamInfo

admin.site.register(
    TeamInfo
)  # register the TeamInfo model so it may be accessed by admin
