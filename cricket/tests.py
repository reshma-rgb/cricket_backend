from django.test import TestCase
from cricket.models import Team,Player,Match,Points
from django.urls import reverse

class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(team_name="Indians", team_logo="static/mi.png",team_state="Maharashtra")

    def test_object(self):
        """check object"""
        obj = Team.objects.get(team_name="Indians")
        #can write more assert
        self.assertEqual(obj.team_state, 'Maharashtra')

class TeamViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_teams = 2

        for id in range(number_of_teams):
            Team.objects.create(
                team_name=f'Team {id}',
                team_state=f'State {id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_objects(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['object_list']) == 2)

class PlayerTestCase(TestCase):
    def setUp(self):
        Team.objects.create(team_name="Knight", team_logo="static/kkr.jpg",team_state="MP")
        team = Team.objects.get(team_name="Knight")
        Player.objects.create(fname="Reshma", lname="Patil",jersey_num=79, pic="static/ab.png",country="India",team =team)

    def test_object(self):
        """check object"""
        obj = Player.objects.get(fname="Reshma")
        self.assertEqual(obj.lname, 'Patil')
        #can write more assert

class PointsTestCase(TestCase):
    def setUp(self):
        Points.objects.create(team="Around",points=7)

    def test_object(self):
        """check object"""
        obj = Points.objects.get(team="Around")
        self.assertEqual(obj.points, 7)
        #can write more assert
