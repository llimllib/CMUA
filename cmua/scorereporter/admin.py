from cmua.scorereporter.models import ScoreReport, Game, Team
from django.contrib import admin

class ScoreReportAdmin(admin.ModelAdmin):
    readonly_fields = ("report_date",)

admin.site.register(ScoreReport, ScoreReportAdmin)
admin.site.register(Game)
admin.site.register(Team)
