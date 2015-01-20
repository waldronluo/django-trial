from django.db import models
from django.contrib import admin

# Create your models here.
class p_block(models.Model):
    title = models.CharField(max_length=150)

class p_list_item (models.Model):
    block = models.ForeignKey(p_block, related_name='block_belonged')
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    content = models.TextField()
    beginDate = models.DateField()
    endDate = models.DateField()


admin.site.register(p_block)
admin.site.register(p_list_item)
