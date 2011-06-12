# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        l = orm.League(name="Summer League 2011", year="2011", active=True, season="summer")
        l.save()

        #set this league as the default for all teams, in preperation for setting the foreignkey
        #as non-null
        for team in orm.Team.objects.all():
            team.league = l
            team.save()


    def backwards(self, orm):
        "Write your backwards methods here."
        #leave this blank; we'll drop the league table on the next back anyway.
        pass


    models = {
        'scorereporter.game': {
            'Meta': {'object_name': 'Game'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team1'", 'to': "orm['scorereporter.Team']"}),
            'team1_points': ('django.db.models.fields.IntegerField', [], {}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team2'", 'to': "orm['scorereporter.Team']"}),
            'team2_points': ('django.db.models.fields.IntegerField', [], {})
        },
        'scorereporter.league': {
            'Meta': {'object_name': 'League'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'scorereporter.scorereport': {
            'Meta': {'object_name': 'ScoreReport'},
            'game1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game1'", 'null': 'True', 'to': "orm['scorereporter.Game']"}),
            'game1_points': ('django.db.models.fields.IntegerField', [], {}),
            'game2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game2'", 'null': 'True', 'to': "orm['scorereporter.Game']"}),
            'game2_points': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opponent1'", 'to': "orm['scorereporter.Team']"}),
            'opponent1_points': ('django.db.models.fields.IntegerField', [], {}),
            'opponent2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opponent2'", 'to': "orm['scorereporter.Team']"}),
            'opponent2_points': ('django.db.models.fields.IntegerField', [], {}),
            'report_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'reporting_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reporting_team'", 'to': "orm['scorereporter.Team']"})
        },
        'scorereporter.team': {
            'Meta': {'object_name': 'Team'},
            'captains': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scorereporter.League']", 'null': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scorereporter']
