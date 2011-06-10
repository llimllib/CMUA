from django import forms

from cmua.scorereporter.models import ScoreReport, Team

class ScoreReportForm(forms.ModelForm):
    class Meta:
        model = ScoreReport
        fields = ('reporting_team', 'game1_points', 'opponent1', 'opponent1_points', 'game2_points', 'opponent2', 'opponent2_points')
        _ns = map(str, range(25))
        _scorechoices = tuple(zip(_ns, _ns))
        widgets = {
            'game1_points': forms.Select(choices=_scorechoices),
            'game2_points': forms.Select(choices=_scorechoices),
            'opponent1_points': forms.Select(choices=_scorechoices),
            'opponent2_points': forms.Select(choices=_scorechoices)
        }
