from django.db import models
from ckeditor.fields import RichTextField

class myCKEditor(models.Model):
    id  = models.AutoField(primary_key=True)
    html_data = RichTextField()


