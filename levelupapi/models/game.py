from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    description = models.CharField(max_length=75)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    maker = models.TextField()
    skill_level = models.IntegerField()

    def __str__(self):
        return self.name
