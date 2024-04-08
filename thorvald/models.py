from django.db import models


class Fighter(models.Model):
    name = models.CharField(max_length=100)
    strength = models.IntegerField()
    fullHP = models.IntegerField()
    maxHP = models.IntegerField()
    armor = models.IntegerField()
    avatar = models.URLField()
    XP = models.IntegerField()
    level = models.IntegerField()
    isDead = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "thorvald"
