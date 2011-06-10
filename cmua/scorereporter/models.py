from django.db import models
from django.contrib import admin

class Team(models.Model):
    captains = models.CharField(max_length=1024, verbose_name="Captains")
    team_name = models.CharField(max_length=1024, verbose_name="Team Name", null=True, blank=True)
    color = models.CharField(max_length=1024, verbose_name="Color", null=True, blank=True)

    def captain_or_name(self):
        return self.team_name if self.team_name else self.captains

    def __unicode__(self):
        return self.captain_or_name()

admin.site.register(Team)

class ScoreReport(models.Model):
    reporting_team = models.ForeignKey(Team, verbose_name="What team are you?", related_name="reporting_team")

    opponent1 = models.ForeignKey(Team, verbose_name="Who was your opponent?", related_name="opponent1")
    opponent2 = models.ForeignKey(Team, verbose_name="Who was your opponent?", related_name="opponent2")

    game1_points = models.IntegerField(verbose_name="How many points did you score?")
    game2_points = models.IntegerField(verbose_name="How many points did you score?")

    opponent1_points = models.IntegerField(verbose_name="How many points did your opponent score?")
    opponent2_points = models.IntegerField(verbose_name="How many points did your opponent score?")

    report_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s vs. %s and %s" % (self.reporting_team, self.opponent1, self.opponent2)
