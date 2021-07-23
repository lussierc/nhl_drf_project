"""Configure teams app."""

from django.apps import AppConfig


class TeamsConfig(AppConfig):
    """Configure teams app & set the default_auto_field for cases where there is no primary key or an auto key is needed."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "teams"
