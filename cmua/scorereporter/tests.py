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

    def test_check_score(self):
        team1 = Team.objects.get(pk=1)
        team2 = Team.objects.get(pk=3)
        g = Game.objects.get(pk=2)

        self.assertEqual(g.team1_points, 13)
        self.assertEqual(g.team2_points, 1)

        #first we'll check a score with a smaller diff, which should change
        #the game's score
        g.check_score(team1, 13, team2, 2)

        #let's reload the object to make sure we didn't just change it in memory
        g = Game.objects.get(pk=2)

        self.assertEqual(g.team1_points, 13)
        self.assertEqual(g.team2_points, 2)

        #next we'll check a score with a greater diff, which should not change
        #the game's score
        g.check_score(team1, 13, team2, 1)

        g = Game.objects.get(pk=2)

        self.assertEqual(g.team1_points, 13)
        self.assertEqual(g.team2_points, 2)
