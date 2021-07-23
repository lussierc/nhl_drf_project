"""Performs serialization tasks on models."""

from rest_framework import serializers

from .models import TeamInfo


class TeamInfoSerializer(serializers.ModelSerializer):
    """Serializes the TeamInfo model."""

    class Meta:
        model = TeamInfo
        fields = [
            "pk",
            "franchise",
            "league",
            "year_established",
            "years_in_operation",
            "games_played",
            "wins",
            "losses",
            "ties",
            "ot_losses",
            "points",
            "points_percentage",
            "playoff_years",
            "division_wins",
            "conference_wins",
            "stanley_cups_won",
            "logo_image_link",
        ]

        # automates the setting of nonrequired fields, using a for loop:
        extra_kwargs = {}
        for nonrequired_field in fields[5:]:
            extra_kwargs[nonrequired_field] = {"required": False}
