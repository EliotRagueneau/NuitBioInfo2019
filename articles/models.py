from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Rubric(models.Model):
    name = models.CharField(max_length=42)


class Topic(models.Model):
    name = models.CharField(max_length=42)
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, related_name='topics')


class Article(models.Model):
    name = models.CharField(max_length=42)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name='articles')
    content = models.TextField()
    creation_date = models.DateField(auto_created=True)
    modification_date = models.DateField(auto_now=True)
    author = models.ForeignKey('Profil', on_delete=models.SET_NULL)


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)  # La liaison OneToOne vers le modèle User

    def __str__(self):
        return "Profil de {0}".format(self.user.username)


class ExternalLink(models.Model):
    pass


class Document(models.Model):
    owner = models.ForeignKey(Profil, on_delete=models.CASCADE)

class KeyWords(models.Model):
    pass
