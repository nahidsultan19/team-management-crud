from django.db import models

# Create your models here.

TEAM_LEVELS = (
    ('U09', 'Under 09s'),
    ('U10', 'Under 10s'),
    ('U11', 'Under 11s'),

)


class Team(models.Model):
    team_name = models.CharField(max_length=40)
    team_level = models.CharField(
        max_length=3, choices=TEAM_LEVELS, default='U11')

    def __str__(self):
        return self.team_name
