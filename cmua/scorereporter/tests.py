from django.test import TestCase

from scorereporter.models import Team, Game, ScoreReport

class GameTestCase(TestCase):
    fixtures = ['scorereporter_testdata.json']

    def test_find_game(self):
        team1 = Team.objects.get(pk=1)
        team2 = Team.objects.get(pk=2)
        g = Game.objects.find_game(team1, team2)
        self.assertEqual(type(g), Game)
        self.assertEqual(g.team1, team1)
        self.assertEqual(g.team1_points, 1)
        self.assertEqual(g.team2, team2)
        self.assertEqual(g.team2_points, 2)

        g = Game.objects.find_game(team2, team1)
        self.assertEqual(type(g), Game)
        self.assertEqual(g.team1, team1)
        self.assertEqual(g.team1_points, 1)
        self.assertEqual(g.team2, team2)
        self.assertEqual(g.team2_points, 2)
