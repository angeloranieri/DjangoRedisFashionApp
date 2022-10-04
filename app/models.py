from django.db import models
from django.conf import settings
from django.utils import timezone
from .utils import send_transaction
import json

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, default=True)
    description = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Owner(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    codeItem = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    change_date = models.DateTimeField(blank=True, null=True)
    txId = models.CharField(max_length=66, blank=True, null=True)

    def __str__(self):
        return self.nickname

    def publish(self):
        self.change_date = timezone.now()
        self.save()

    def save(self):
        self.txId = self.write_on_chain()
        super(Owner, self).save()

    def write_on_chain(self):
        jsonObj = {}
        jsonObj["item"] = self.codeItem
        jsonObj["owner"] = self.nickname
        return send_transaction(json.dumps(jsonObj))










