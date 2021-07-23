"""Perform model creation process."""

from django.db import models


class TeamInfo(models.Model):
    """Defines schema for TeamInfo model."""

    franchise = models.CharField(max_length=60, null=False)
    league = models.CharField(max_length=30, null=False)
    year_established = models.IntegerField(null=False)
    years_in_operation = models.IntegerField(null=False)
    games_played = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    ties = models.IntegerField(null=True)
    ot_losses = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    points_percentage = models.CharField(max_length=10, null=True)
    playoff_years = models.IntegerField(null=True)
    division_wins = models.IntegerField(null=True)
    conference_wins = models.IntegerField(null=True)
    stanley_cups_won = models.IntegerField(null=True)
    logo_image_link = models.CharField(max_length=250, null=True)

    def __str__(self):
        """Returns franchise name so it is displayed on admin site instead of numerical pk id."""
        return self.franchise

    def get_team_info_dict(self):
        """Returns a dictionary of team information for easy access, especially for testing purposes."""
        return {
            "franchise": self.franchise,
            "league": self.league,
            "year_established": self.year_established,
            "years_in_operation": self.years_in_operation,
            "games_played": self.games_played,
            "wins": self.wins,
            "losses": self.losses,
            "ties": self.ties,
            "ot_losses": self.ot_losses,
            "points": self.points,
            "points_percentage": self.points_percentage,
            "playoff_years": self.playoff_years,
            "division_wins": self.division_wins,
            "conference_wins": self.conference_wins,
            "stanley_cups_won": self.stanley_cups_won,
            "logo_image_link": self.logo_image_link,
        }
