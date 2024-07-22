from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdmissionForm(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    school = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    certificate = models.FileField(upload_to='certificates/')
    declaration = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
