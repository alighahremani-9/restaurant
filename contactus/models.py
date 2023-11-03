from django.db import models

# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"post-{self.id}: {self.body}"