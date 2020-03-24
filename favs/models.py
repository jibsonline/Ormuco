from django.db import models


class FavDetails(models.Model):
    firstName = models.CharField("Name", max_length=255, blank=False, null=False, unique=True)
    favColor = models.CharField("Favorite Color", max_length=255, blank=False, null=False)
    catsOrDogs = models.CharField("Cats or Dogs", max_length=255, blank=False, null=False)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.firstName
