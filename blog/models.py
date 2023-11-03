from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # picture = models.ImageField(upload_to="profile/")
    # bio = models.TextField()


@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    # print(sender.username)
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()

class Book(models.Model):
    # auther = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.DecimalField(max_digits=10, decimal_places=1)
    def __str__(self):
        return f"post-{self.id}: {self.name}"