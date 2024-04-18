from django.contrib import admin

# Register your models here.

from Register.models import Player,Team,Match

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
