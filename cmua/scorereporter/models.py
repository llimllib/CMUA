from django.db.models import Model, CharField, ForeignKey, IntegerField, DateTimeField
from django.contrib import admin

class Team(Model):
    captains = CharField(max_length=1024, verbose_name="Captains")
    team_name = CharField(max_length=1024, verbose_name="Team Name", null=True, blank=True)
    color = CharField(max_length=1024, verbose_name="Color", null=True, blank=True)

    def captain_or_name(self):
        return self.team_name if self.team_name else self.captains

    def __unicode__(self):
        return self.captain_or_name()

admin.site.register(Team)

class ScoreReport(Model):
    reporting_team = ForeignKey(Team, verbose_name="What team are you?", related_name="reporting_team")

    opponent1 = ForeignKey(Team, verbose_name="Who was your opponent?", related_name="opponent1")
    opponent2 = ForeignKey(Team, verbose_name="Who was your opponent?", related_name="opponent2")

    game1_points = IntegerField(verbose_name="How many points did you score?")
    game2_points = IntegerField(verbose_name="How many points did you score?")

    opponent1_points = IntegerField(verbose_name="How many points did your opponent score?")
    opponent2_points = IntegerField(verbose_name="How many points did your opponent score?")

    report_date = DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s vs. %s and %s" % (self.reporting_team, self.opponent1, self.opponent2)
