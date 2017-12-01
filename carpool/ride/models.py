from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    picture = modelsImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    work = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
