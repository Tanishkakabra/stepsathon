from django.db import models
import uuid

from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    unique_ticket_number = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.unique_ticket_number)

