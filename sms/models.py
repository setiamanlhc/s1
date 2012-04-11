from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    group = models.BooleanField()
    mobileno = models.CharField(max_length=20)
    user = models.ForeignKey(User)

    class Meta:
        db_table = "Contact"
        
    def __unicode__(self):
        return self.name

class Sender(models.Model):
    name = models.CharField(max_length=15)
    user = models.ForeignKey(User)
    
    class Meta:
        db_table = "Sender"
        
    def __unicode__(self):
        return self.name
