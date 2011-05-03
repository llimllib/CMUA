from cmua.registration.models import Register
from django.contrib import admin

class RegisterAdmin(admin.ModelAdmin):
    readonly_fields = ("last_modified", "date_created")

admin.site.register(Register, RegisterAdmin)
