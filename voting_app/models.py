from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Constituency(models.Model):
    name= models.CharField(max_length=30, blank=False)
    def __str__(self):
        return self.name
class Candidate(models.Model):
    name=models.CharField(max_length=30, blank=False)
    Constituency=models.ForeignKey(Constituency, on_delete=models.CASCADE)
    no_votes=models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
class VoterDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    voted=models.BooleanField(default=False)
    Constituency=models.ForeignKey(Constituency, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username