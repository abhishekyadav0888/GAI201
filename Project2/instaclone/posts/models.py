from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=100)
    caption = models.TextField()

    def __str__(self):
        return self.caption
