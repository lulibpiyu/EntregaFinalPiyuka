from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class CodingGame(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    time_estimated = models.IntegerField()
    code_snippet = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_enabled = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title