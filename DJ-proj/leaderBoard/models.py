from django.db import models

# Create your models here.
#class player_scores(models.Model):
#    name = models.CharField(max_length = 100)
#    score = models.IntegerField()


class PlayerScores(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    game_record_id = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'player_scores'
    
class TestTable(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    massege = models.TextField(max_length=200, blank=True)
    numbers = models.IntegerField(blank=True, null=True)

        
        