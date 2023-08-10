from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  emailid = models.CharField(max_length=255, null=True)
  dateofbirth = models.DateField(null=True)
