from django.core.management.base import BaseCommand

from cmua.scorereporter.models import ScoreReport, Team, Game

class Command(BaseCommand):
    help = "Make Games from ScoreReports"

    def handle(self, *args, **options):
        #pseudocode:
        #for score in scorereports where game1=null or game2=null
        #   if not game1:
        #       try to find this game already reported and set game1=game
        #       otherwise create a new game
        #   repeat for game2
        #
        #TODO: handle team1 playing team2 a second time?
        for s in ScoreReport.objects.filter(game1__isnull=True):
            g = Game.objects.find_game(s.reporting_team, s.opponent1)

            if not g:
                g = Game(team1=s.reporting_team, team1_points=s.game1_points,
                         team2=s.opponent1,      team2_points=s.opponent1_points)
            else:
                g.check_score(s.reporting_team, s.game1_points, s.opponent1, s.opponent1_points)

            s.game1 = g

            g.save()
            s.save()

        for s in ScoreReport.objects.filter(game2__isnull=True):
            g = Game.objects.find_game(s.reporting_team, s.opponent2)

            if not g:
                g = Game(team1=s.reporting_team, team1_points=s.game2_points,
                         team2=s.opponent2,      team2_points=s.opponent2_points)
            else:
                g.check_score(s.reporting_team, s.game2_points, s.opponent2, s.opponent2_points)

            s.game2 = g

            g.save()
            s.save()
