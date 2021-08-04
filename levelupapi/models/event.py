from django.db import models


class Event(models.Model):
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField("%Y-%m-%d")
    time = models.TimeField("%H:%M")
    description = models.TextField()
    attendees = models.ManyToManyField(
        "Gamer", through="EventGamer", related_name="attending")

    def __str__(self) -> str:
        return f'{self.game.name} on {self.date} hosted by {self.host}'
