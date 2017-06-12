from django.db import models

class Person(models.Model):
    owner_name = models.CharField(max_length=130)
    owner_friends = models.ManyToManyField('self')
    owner_suggestion = models.ManyToManyField('self')

    def __str__(self):
        return self.owner_name


