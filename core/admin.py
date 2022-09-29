from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.StaffMember)
admin.site.register(models.Request)
admin.site.register(models.Project)
admin.site.register(models.Job)
admin.site.register(models.JobType)
admin.site.register(models.Task)
admin.site.register(models.SiteDiary)
