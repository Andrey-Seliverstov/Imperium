from django.db import models
from users.models import Profile


class SpaceMarines(models.Model):
    symbol = models.ImageField(upload_to='Space_Marines/images/', default='default_image.jpg')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Space_Marines/images/', default='default_icon.png')

    def __str__(self):
        return self.title


class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order = models.ForeignKey(SpaceMarines, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Review by {self.owner}"
