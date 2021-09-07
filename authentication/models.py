from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.URLField(default='https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mm')
    status = models.CharField(max_length=20)