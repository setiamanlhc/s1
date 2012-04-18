from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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

class SMS(models.Model):
    sender = models.ForeignKey(Sender)
    user = models.ForeignKey(User)
    message = models.CharField('Message', max_length=160, help_text='enter @SN to replace it with short name of contact')
    groups = models.ManyToManyField(Group, blank=True, null=True)
    contacts = models.ManyToManyField(Contact,blank=True, null=True)
    senton = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "SMS"
        verbose_name = _('SMS')
        verbose_name_plural = _('Send SMS')
        
    def __unicode__(self):
        return self.message
"""
    def clean(self):
        from django.core.exceptions import ValidationError
        # Don't allow draft entries to have a pub_date.
        if self.contacts is None and self.groups is None:
            raise ValidationError('Either Group or Contact is empty')
   """     
            
