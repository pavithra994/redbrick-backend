from django.db import models
from user.models import User

# Create your models here.
class JobType(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=30)
    description = models.CharField(max_length=255,null=True,blank=True)

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Staff(models.Model):
    STAFF_ROLE = [
        ("ADMIN","Admin Staff"),
        ("MANAGER","Manager"),
        ("SUPERVISOR","Supervisor"),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=100,choices=STAFF_ROLE,default="SUPERVISOR")

# class Guest(models.Model):
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(null=True,blank=True)

class Request(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("ON_PROGRESS", "ON_PROGRESS"),
    ]
    job_type = models.ForeignKey("JobType",on_delete=models.CASCADE,related_name="request_related")
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField(null=True,blank=True)
    guest_phone = models.EmailField(null=True,blank=True)
    client = models.ForeignKey("Client",on_delete=models.CASCADE,null=True,blank=True)
    is_reviewed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    reviewed_by =  models.ForeignKey("Staff",on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="PENDING")
    created_date = models.DateTimeField(auto_created=True)



class Project(models.Model):
    manager = models.ForeignKey("Staff",on_delete=models.CASCADE)
    client = models.ForeignKey("Client",on_delete=models.CASCADE)
    location = models.CharField(max_length=500,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    created_date = models.DateTimeField(auto_created=True)


class Job(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("COMPLETED", "COMPLETED"),
        ("CLOSED", "Payments closed"),
        ("ON_PROGRESS", "ON_PROGRESS"),
    ]
    supervisor = models.ForeignKey("Staff",on_delete=models.CASCADE)
    project = models.ForeignKey("Project",on_delete=models.CASCADE)
    description = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="PENDING")
    created_date = models.DateTimeField(auto_created=True)


class Task(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("COMPLETED", "COMPLETED"),
        ("CLOSED", "Payments closed"),
        ("ON_PROGRESS", "ON_PROGRESS"),
    ]
    supervisor = models.ForeignKey("Staff",on_delete=models.CASCADE)
    job = models.ForeignKey("Job",on_delete=models.CASCADE)
    description = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="PENDING")
    last_update = models.DateTimeField(auto_now=True)


class SiteDiary(models.Model):
    supervisor = models.ForeignKey("Staff", on_delete=models.CASCADE)
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
