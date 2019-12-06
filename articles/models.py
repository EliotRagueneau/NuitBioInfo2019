from django.db import models
from django.contrib.auth.models import User
import datetime


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
    models.ManyToManyField('DocumentType', related_name='necessary_to')


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)  # La liaison OneToOne vers le modèle User

    def __str__(self):
        return "{}_{}".format(self.user.last_name.upper(), self.user.first_name.capitalize())


class ExternalLink(models.Model):
    link = models.URLField()


class DocumentType(models.Model):
    name = models.CharField(max_length=42)
    delay_of_acquisition = models.TimeField()

    def __str__(self):
        return self.name


class Document(models.Model):
    owner = models.ForeignKey(Profil, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)

    def handle_file(self, filename):
        return "documents/{}/{}_{}.{}".format(self.owner.id, self.type, self.owner, filename.split('.')[-1])

    file = models.FileField(upload_to=handle_file)

    def warn_user(self):
        if self.expiry_date < datetime.datetime.now().time() + self.type.delay_of_acquisition:
            self.owner.user.email


class KeyWords(models.Model):
    name = models.CharField(max_length=42)
