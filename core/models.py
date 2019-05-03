from django.db import models
import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class League(models.Model):
    all_leagues = ([('english','english league'),('spanish','spanish league'),('italian','italian league'),
                ('french','french league'),('german','german league'),
                ('champions','champions league'),('egyptian','egyptian league')])
    leagues = models.CharField(max_length=100, choices=all_leagues)
    name_ar =models.CharField(max_length=100, default="الدوري")

    def __str__(self):
        return self.leagues


class Club(models.Model):
    league_names = models.ForeignKey(League, on_delete= models.CASCADE, related_name='club')
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='media/core', max_length=255, null=True, blank=True)
    year_of_establishment = models.IntegerField(default=1900)
    won = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    goal_for = models.IntegerField(default=0)
    goal_against = models.IntegerField(default=0)


    def CalcPoints(self):
        # type/value check solution for TypeError : Unsupported operand type(S): nontype and nontype
        #if self.won and self.draw and self.won !=0 and self.draw != 0:
           return self.won*3 + self.draw            

    total_points = property(CalcPoints)

    def GoalDiff(self):
            return self.goal_for - self.goal_against

    goal_diff = property(GoalDiff)

    def __str__(self):
        return self.name



class LeagueNews(models.Model):
    league_names = models.ForeignKey(League, on_delete=models.CASCADE, related_name='news')
    news_title = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    news_text = models.TextField()
    news_image = models.ImageField(upload_to='media/core',max_length=255, null=True,blank=True)
    clubs = models.ManyToManyField(Club , related_name='news')

    def __str__(self):
        return self.news_title
    
    

class Comment(models.Model):
    leaguenews = models.ForeignKey(LeagueNews, on_delete= models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text


class Match(models.Model):
    play_date = models.DateTimeField('play date')
    occasion = models.ForeignKey(League, on_delete=models.CASCADE, related_name='match')
    club_visitor = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='match_club_visitor')
    club_local = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='match_club_local')
    score_visitor = models.IntegerField()
    score_local = models.IntegerField()


@receiver(post_save, sender=Match)
def update_club_score(instance, sender, **kwargs):
    instance.club_local.goal_for += instance.score_local
    instance.club_local.goal_against += instance.score_visitor
    instance.club_visitor.goal_for += instance.score_visitor
    instance.club_visitor.goal_against += instance.score_local
    # club local won
    if instance.score_local > instance.score_visitor:
        instance.club_local.won += 1
        instance.club_local.save()
        instance.club_visitor.lost += 1
        instance.club_visitor.save()
    # club local lost
    if instance.score_local < instance.score_visitor:
        instance.club_local.lost += 1
        instance.club_local.save()
        instance.club_visitor.won += 1
        instance.club_visitor.save()
    # draw
    if instance.score_local == instance.score_visitor:
        instance.club_local.draw += 1
        instance.club_local.save()
        instance.club_visitor.draw += 1
        instance.club_visitor.save()


