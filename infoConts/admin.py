from django.contrib import admin
from .models import LastInfo

# Register your models here.


class LastInfoAdmin(admin.ModelAdmin):

    list_display = ("title", "date", "time", "team_staff")
    search_fields = ["date", "time", "team_staff"]


admin.site.register(LastInfo, LastInfoAdmin)
