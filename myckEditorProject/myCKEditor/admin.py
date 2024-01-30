from django.contrib import admin
from .models import myCKEditor

class myCKEditor_Admin(admin.ModelAdmin):
    list_display = ['id','html_data']
    
admin.site.register(myCKEditor,myCKEditor_Admin)

