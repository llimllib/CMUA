from cmua.scorereporter.models import ScoreReport
from django.contrib import admin

class ScoreReportAdmin(admin.ModelAdmin):
    readonly_fields = ("report_date",)

admin.site.register(ScoreReport, ScoreReportAdmin)
