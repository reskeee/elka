from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):

    STATUS_CHOISES = [
        ('active', 'Активныне'),
        ('completed', 'Завершенный')
    ]

    title = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to='events_images/')
    event_datetime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, default='active')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Myevent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'