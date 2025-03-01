from django.db import models


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

    def __str__(self):
        return self.title