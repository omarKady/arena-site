from django.contrib import admin

# Register your models here.

from .models import League, LeagueNews, Comment, Club, Match
admin.site.register(League)
admin.site.register(LeagueNews)
admin.site.register(Comment)

class ClubAdmin(admin.ModelAdmin):
    fields = ['league_names', 'name', 'year_of_establishment', 'logo', 'won', 'draw', 'lost', 'total_points', 'goal_for', 'goal_against', 'goal_diff']
    readonly_fields = ('total_points', 'goal_diff',)

admin.site.register(Club, ClubAdmin)
admin.site.register(Match)