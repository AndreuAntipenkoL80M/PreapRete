from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#class player_scores(models.Model):
#    name = models.CharField(max_length = 100)
#    score = models.IntegerField()


class PlayerScores(models.Model):
    userkey = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=User._meta.get_field('username').max_length, blank=True, null=True)
    name = models.CharField(max_length=40, blank=False, null=False, default='toDelete')
    score = models.IntegerField(blank=False, null=False, default=0)
    game_record_id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'player_scores'
    
class TestTable(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    massege = models.TextField(max_length=200, blank=True)
    numbers = models.IntegerField(blank=True, null=True)

        
        