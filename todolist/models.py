from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField()
    deadline = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
