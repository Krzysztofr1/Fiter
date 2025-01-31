from django.db import models

from django.contrib.auth.models import User

class SurveyData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body_mass = models.FloatField()  # masa ciała
    height = models.FloatField()  # wysokość ciała
    body_fat = models.FloatField(null=True, blank=True)  # zawartość tkanki tłuszczowej
    cell_mass = models.FloatField(null=True, blank=True)  # zawartość masy komórkowej
    fat_free_mass = models.FloatField(null=True, blank=True)  # zawartość masy beztłuszczowej
    muscle_mass = models.FloatField(null=True, blank=True)  # zawartość masy mięśniowej

    def __str__(self):
        return f"Survey Data for {self.user.username}"