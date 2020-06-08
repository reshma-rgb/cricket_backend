from django.contrib import admin
from cricket.models import Team,Player,PlayerHistory,Match,Points

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayerHistory)
admin.site.register(Match)
admin.site.register(Points)
