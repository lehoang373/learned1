from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey, \
    ChainedManyToManyField, GroupedForeignKey

# Create your models here.
class Lesson(models.Model):
    projectnumber = models.CharField(max_length=255)
    projectname = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    projectlocation = models.CharField(max_length=255)
    description = models.TextField()
    division = models.CharField(max_length=20)
    marketsector = models.CharField(max_length=255)
    discipline = models.CharField(max_length=20)
    author = models.CharField(max_length=100)
    memo = models.CharField(max_length=255)
    linkfile = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author)

