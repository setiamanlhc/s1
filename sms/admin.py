#Admin.py
#Developed by Setiaman, 09-04-2012
from datetime import datetime
from django.contrib import admin
from models import Contact, Sender, Group, Country
from models import SMS
from django import forms

class ModelManager(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()
    
class ContactAdmin(ModelManager):
    exclude = ('user',)
    list_display = ('name','mobileno')
    search_fields = ['name','mobileno']

 
    def queryset(self, request):
        if request.user.is_superuser:
            #return Contact.objects.all()
            return self.model._default_manager.all()
        return self.model._default_manager.filter(user=request.user)
    
#        return Contact.objects.filter(user=request.user)


class SenderAdmin(ModelManager):
    exclude = ('user',)
    list_display = ('name',)
    search_fields = ['name']

    def queryset(self, request):
        if request.user.is_superuser:
            return Sender.objects.all()
        return Sender.objects.filter(user=request.useradmin.site.register(Contact, ContactAdmin))
  

class GroupAdmin(ModelManager):
    exclude = ('user',)
    list_display = ('name',)
    search_fields = ['name']
    filter_horizontal = ('members',)

    def queryset(self, request):
        if request.user.is_superuser:
            return Group.objects.all()
        return Group.objects.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(GroupAdmin,self).get_form(request, obj,**kwargs)
        form.base_fields['members'].queryset = form.base_fields['members'].queryset.filter(user=request.user)
        return form
    
class SMSAdminForm(forms.ModelForm):
    class Meta:
        model = SMS

        

    
class SMSAdmin(ModelManager):
    #form = SMSAdminForm
    exclude = ('user','contacts')
    list_display = ('sender','senton',)
    search_fields = ['sender']
    filter_horizontal = ('groups',)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=True)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()
        
    
"""
    def queryset(self, request):
        if request.user.is_superuser:
            return SMS.objects.all()
        return SMS.objects.filter(user=request.user)    
"""        

admin.site.register(Country)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Sender, SenderAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(SMS, SMSAdmin)


