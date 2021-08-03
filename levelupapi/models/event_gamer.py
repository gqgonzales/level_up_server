from django.db import models


class EventGamer(models.Model):
    """
    Join model for Events and Gamers
    """
    event = models.ForeignKey("event", on_delete=models.CASCADE)
    gamer = models.ForeignKey("gamer", on_delete=models.CASCADE)
