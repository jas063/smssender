from django.contrib import admin
from addnew.models import add,Message
# Register your models here.


class addnewadmin(admin.ModelAdmin):
    fields = ['fname','mobile','email','dob','marriageaniversary','remarks']

admin.site.register(add,addnewadmin)

class messageadmin(admin.ModelAdmin):
    fields = ['name','sentTo','date','time','message']

admin.site.register(Message,messageadmin)
