from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.user.username

def save_post(sender,**kwargs):
    if kwargs['created']:
        p1 = Profile(user=kwargs['instance'])
        p1.save()


post_save.connect(save_post,sender=User)

