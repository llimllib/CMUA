from django.db.models.query import QuerySet
from django.db.models import Model, Manager, Q, CharField, ForeignKey, IntegerField, DateTimeField
from django.contrib import admin

class Team(Model):
    captains = CharField(max_length=1024, verbose_name="Captains")
    team_name = CharField(max_length=1024, verbose_name="Team Name", null=True, blank=True)
    color = CharField(max_length=1024, verbose_name="Color", null=True, blank=True)

    def captain_or_name(self):
        return self.team_name if self.team_name else self.captains

    @property
    def all_games(self):
        return self.team1.all() | self.team2.all()

    @property
    def standings(self):
        wins = 0
        losses = 0
        for game in self.all_games:
            if game.win(self):
                wins += 1
            else:
                losses += 1
        if wins or losses:
            return (float(wins)/(wins+losses), wins, losses, self.captains, self.team_name, self.pk)
        else:
            return (0,0,0, self.captains, self.team_name, self.pk)

    def __unicode__(self):
        return self.captain_or_name()

class GameManager(Manager):
    def find_game(self, team1, team2):
        """return a game or None"""
        game = QuerySet(self.model, using=self._db).filter(
            Q(team1__exact=team1, team2__exact=team2) |
            Q(team1__exact=team2, team2__exact=team1))
        return game[0] if game else None

class Game(Model):
    team1 = ForeignKey(Team, related_name="team1")
    team2 = ForeignKey(Team, related_name="team2")

    team1_points = IntegerField()
    team2_points = IntegerField()

    objects = GameManager()

    def win(self, team):
        if self.team1 == team:
            return self.team1_points > self.team2_points
        return self.team1_points < self.team2_points

    def check_score(self, team1, team1_points, team2, team2_points):
        #if the score reports are different, favor the score report with the
        #lesser score difference
        if abs(team1_points - team2_points) < abs(self.team1_points - self.team2_points):
            if team1 == self.team1:
                self.team1_points = team1_points
                self.team2_points = team2_points
            else:
                self.team2_points = team1_points
                self.team1_points = team2_points

            self.save()

    def __unicode__(self):
        return "%s %s %s %s" % (self.team1, self.team1_points, self.team2, self.team2_points)

class ScoreReport(Model):
    reporting_team = ForeignKey(Team, verbose_name="What team are you?", related_name="reporting_team")

    opponent1 = ForeignKey(Team, verbose_name="Who was your opponent?", related_name="opponent1")
    opponent2 = ForeignKey(Team, verbose_name="Who was your opponent?", related_name="opponent2")

    game1_points = IntegerField(verbose_name="How many points did you score?")
    game2_points = IntegerField(verbose_name="How many points did you score?")

    opponent1_points = IntegerField(verbose_name="How many points did your opponent score?")
    opponent2_points = IntegerField(verbose_name="How many points did your opponent score?")

    game1 = ForeignKey(Game, blank=True, null=True, related_name="game1")
    game2 = ForeignKey(Game, blank=True, null=True, related_name="game2")

    report_date = DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s vs. %s and %s" % (self.reporting_team, self.opponent1, self.opponent2)
