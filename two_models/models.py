from django.db import models


class Notes(models.Model):
    Title = models.CharField(max_length=20, unique=True)
    Text = models.TextField(max_length=255)
    Created_At = models.TimeField()

    def __str__(self):
        return self.Title


class Tags(models.Model):
    Tag_Name = models.CharField(Notes, max_length=20)
    Description = models.TextField(max_length=255)
    Notes_Title = models.ManyToManyField('Notes')

    def __str__(self):
        return self.Tag_Name

