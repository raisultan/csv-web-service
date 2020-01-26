from django.contrib import admin

from . import models


admin.site.register(models.Item)
admin.site.register(models.Client)
admin.site.register(models.Deal)
admin.site.register(models.DealHistoryFile)
