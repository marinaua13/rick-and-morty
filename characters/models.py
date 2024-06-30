from django.db import models


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "ALIVE"
        DEAD = "DEAD"
        UNKNOWN = "unknown"

    class GenderChoices(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        GENDERLESS = "genderless"
        UNKNOWN = "unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=50, choices=StatusChoices.choices)
    species = models.CharField(max_length=256)
    gender = models.CharField(max_length=50, choices=GenderChoices.choices)
    image = models.URLField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name