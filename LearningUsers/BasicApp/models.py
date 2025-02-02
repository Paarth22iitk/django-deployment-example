from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # add any additional attributes
    portfolio_site = models.URLField(blank=True)
    portfolio_pic = models.ImageField(upload_to="portfolio_pics", null=True, blank=True)

    def __str__(self):
        return self.user.username