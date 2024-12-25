from django.db import models


class History(models.Model):
    DoesNotExist = None
    millennium = models.SmallIntegerField(unique=True)
    description = models.TextField()

    def __str__(self):
        return str(self.millennium)

