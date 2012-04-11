#Admin.py
#Developed by Setiaman, 09-04-2012

from django.contrib import admin
from models import Contact

class ModelManager(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        presave(self, request, obj, form, change)
        obj.save()
        postsave(self, request, obj, form, change)
        
    def presave(self, request, obj, form, change):
        if not change:
            obj.user = request.user
    def postsave(self, request, obj, form, change):
        pass
    
class ContactAdmin(admin.ModelAdmin):
    exclude = ('group','user',)
    list_display = ('name','mobileno')
    search_fields = ['name','mobileno']

    #implement pre-save activity
    def save_model(self, request, obj, form, change):
        if not change:
            obj.group = True
            obj.user = request.user
            
        obj.save()

    def queryset(self, request):
        if request.user.is_superuser:
            return Contact.objects.all()
        return Contact.objects.filter(user=request.user, group=False)

class SenderAdmin(ModelManager):
    exclude = ('user')
    list_display = ('name')
    search_fields = ['name']

    def queryset(self, request):
        if request.user.is_superuser:
            return Sender.objects.all()
        return Sender.objects.filter(user=request.user)
    


admin.site.register(Contact, ContactAdmin)
admin.site.register(Sender, SenderAdmin)

