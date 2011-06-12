# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Team'
        db.create_table('scorereporter_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('captains', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('scorereporter', ['Team'])

        # Adding model 'Game'
        db.create_table('scorereporter_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team1', to=orm['scorereporter.Team'])),
            ('team2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='team2', to=orm['scorereporter.Team'])),
            ('team1_points', self.gf('django.db.models.fields.IntegerField')()),
            ('team2_points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('scorereporter', ['Game'])

        # Adding model 'ScoreReport'
        db.create_table('scorereporter_scorereport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reporting_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reporting_team', to=orm['scorereporter.Team'])),
            ('opponent1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opponent1', to=orm['scorereporter.Team'])),
            ('opponent2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opponent2', to=orm['scorereporter.Team'])),
            ('game1_points', self.gf('django.db.models.fields.IntegerField')()),
            ('game2_points', self.gf('django.db.models.fields.IntegerField')()),
            ('opponent1_points', self.gf('django.db.models.fields.IntegerField')()),
            ('opponent2_points', self.gf('django.db.models.fields.IntegerField')()),
            ('game1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='game1', null=True, to=orm['scorereporter.Game'])),
            ('game2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='game2', null=True, to=orm['scorereporter.Game'])),
            ('report_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('scorereporter', ['ScoreReport'])


    def backwards(self, orm):
        
        # Deleting model 'Team'
        db.delete_table('scorereporter_team')

        # Deleting model 'Game'
        db.delete_table('scorereporter_game')

        # Deleting model 'ScoreReport'
        db.delete_table('scorereporter_scorereport')


    models = {
        'scorereporter.game': {
            'Meta': {'object_name': 'Game'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team1'", 'to': "orm['scorereporter.Team']"}),
            'team1_points': ('django.db.models.fields.IntegerField', [], {}),
            'team2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team2'", 'to': "orm['scorereporter.Team']"}),
            'team2_points': ('django.db.models.fields.IntegerField', [], {})
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
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scorereporter']
