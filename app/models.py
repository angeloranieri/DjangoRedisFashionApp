from django.db import models
from django.conf import settings
from django.utils import timezone

class Owner(models.Model):
    nickname = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nickname

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.ManyToManyField(Owner)
    change_date = models.DateTimeField(blank=True, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def __str__(self):
        return self.code

    def publish(self):
        self.change_date = timezone.now()
        self.save()
