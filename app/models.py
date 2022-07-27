from django.db import models
from django.conf import settings
from django.utils import timezone
from .utils import send_transaction
import json
#import hashlib


class Owner(models.Model):
    nickname = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nickname

    def save(self):
        self.save()

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    owner = models.ManyToManyField(Owner)
    change_date = models.DateTimeField(blank=True, null=True)
    txId = models.CharField(max_length=66, blank=True, null=True)

    def __str__(self):
        return self.code

    def publish(self):
        self.change_date = timezone.now()
        self.save()

    def save(self):
        self.txId = self.write_on_chain()
        super(Item, self).save()

    def write_on_chain(self):

        jsonObj = {}
        jsonObj["code"] = Item.code
        jsonObj["owner"] = Item.owner
        return send_transaction(json.dumps(jsonObj))

        #hash = hashlib.sha256()
        #hash.update(self.code)
        #hash.update(self.owner)
        #hash.hexdigest()
    # item = Item.objects.select_related(jsonObj).get(pk=pk)
    # item.serialize(jsonObj)
    # self.hash = hashlib.sha256(jsonObj.encode('utf-8')).hexdigest()
    # return send_transaction(self.hash)





