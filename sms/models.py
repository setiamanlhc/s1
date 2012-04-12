from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField('Country',max_length=40)
    code = models.CharField('Country Code', max_length=5)
 
    class Meta:
        db_table = "Country"
        
    def __unicode__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=60)
    mobileno = models.CharField('Mobile No',max_length=20)
    user = models.ForeignKey(User)
    country = models.ForeignKey(Country)
    shortname = models.CharField('Short Name',max_length=15)
    
    class Meta:
        db_table = "Contact"
        
    def __unicode__(self):
        return self.name

class Sender(models.Model):
    name = models.CharField('Name',max_length=15)
    user = models.ForeignKey(User)
    
    class Meta:
        db_table = "Sender"
        
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User)
    members = models.ManyToManyField(Contact)
    class Meta:
        db_table = "Group"
        
    def __unicode__(self):
        return self.name

