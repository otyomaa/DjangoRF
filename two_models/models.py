from django.db import models


class Notes(models.Model):
    """ Создаем таблицу Notes с данными """
    Title = models.CharField(max_length=20, unique=True)
    Text = models.TextField(max_length=255)
    Created_At = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.Title


class Tags(models.Model):
    """ Создаем таблицу Tags с данными """
    Tag_Name = models.CharField(max_length=20)
    Description = models.TextField(max_length=255)
    Notes = models.ManyToManyField(Notes, related_name='notes')

    def __str__(self):
        return self.Tag_Name

