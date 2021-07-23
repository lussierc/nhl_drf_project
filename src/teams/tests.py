"""Tests the Django Rest Framework project."""

from django.test import TestCase
from .models import TeamInfo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import TeamInfoSerializer


class TeamInfoTest(TestCase):
    """Testing class for the TeamInfo model & serializer."""

    def setUp(self):
        """Sets up testing TeamInfo & TeamInfoSerializer objects."""
        self.team_info_obj_1 = TeamInfo.objects.create(franchise='Pittsburgh Penguins', league="NHL", year_established="1967", years_in_operation="54")
        self.team_info_obj_2 = TeamInfo.objects.create(franchise='Calgary Flames', league="NHL", year_established=1972, years_in_operation=48, games_played=3790)

        self.obj_1_serializer = TeamInfoSerializer(instance=self.team_info_obj_1)

        self.obj_2_serializer = TeamInfoSerializer(instance=self.team_info_obj_2)


        self.team_info_dict_1 = self.team_info_obj_1.get_team_info_dict()

    def test_model_setup(self):
        """Ensures setup was properly completed."""
        self.assertTrue(self.team_info_dict_1['franchise'] == 'Pittsburgh Penguins')
        self.assertTrue(self.team_info_dict_1['years_in_operation'] == '54')
        self.assertTrue(self.team_info_dict_1['ties'] == None)


    def test_faulty_setups(self):
        """Tests the creation of a TeamInfo object without a required field, ensuring that it fails."""
        try:
            self.team_info_obj_3 = TeamInfo.objects.create(franchise='Seattle Kraken', league="NHL", year_established="1967")
            failed = False
        except:
            failed = True # fails as expected

        self.assertTrue(failed) # ensure creation failed as expected

        failed=None

        try:
            self.team_info_obj_4 = TeamInfo.objects.create(franchise='Allegheny Gators', league="CHE", year_established="1990", years_in_operation="31", points_percentage="thisstringisovermaxallowedchars")
            failed = False
        except:
            failed=True

        self.assertTrue(failed)

    def test_serializer(self):
        """Ensure data was properly serialized."""
        ser_obj_1_data = self.obj_1_serializer.data
        ser_obj_2_data = self.obj_2_serializer.data

        self.assertTrue(ser_obj_1_data['pk'] == 1)
        self.assertTrue(ser_obj_2_data['pk'] == 2)

        self.assertEqual(ser_obj_1_data['franchise'], self.team_info_dict_1['franchise'])
