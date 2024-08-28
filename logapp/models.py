from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    purpose_of_visit = models.TextField()
    host = models.CharField(max_length=100)
    id_verified = models.BooleanField(default=False)
    safety_briefing_acknowledged = models.BooleanField(default=False)
    ppe_issued = models.BooleanField(default=False)
    badge_number = models.CharField(max_length=50, blank=True) 
    arrival_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.arrival_time})"
