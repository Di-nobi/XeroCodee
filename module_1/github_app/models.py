from django.db import models

# Create your models here.
class GithubApp(models.Model):
    name = models.CharField(max_length=100, null=False, default='None')
    public_repo = models.BooleanField(default=True)
    private_repo = models.BooleanField(default=False)
