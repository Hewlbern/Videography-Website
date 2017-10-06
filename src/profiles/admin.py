from django.contrib import admin
from .models import profile


class profileAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    class Meta:
        model = profile


admin.site.register(profile, profileAdmin)