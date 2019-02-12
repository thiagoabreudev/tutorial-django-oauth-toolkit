from django.db import models
from django.conf import settings


class Feed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(verbose_name='Message', max_length=255)
    image = models.ImageField(upload_to="images", verbose_name="Image")

    def __str__(self):
        return self.user.first_name
    
