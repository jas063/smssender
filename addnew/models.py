from django.db import models

# Create your models here.


class add(models.Model):
    fname=models.CharField(max_length=25,blank=False)
    mobile=models.IntegerField(blank=False)
    email=models.EmailField(blank=False)
    dob=models.DateField(max_length=25,blank=False)
    marriageaniversary=models.DateField(blank=False)
    remarks=models.CharField(max_length=100,blank=True)

    def __unicode__(self):
        return self.fname

class Message(models.Model):
    message=models.CharField(max_length=160)
    sentTo=models.IntegerField()
    name=models.CharField(max_length=25)
    date=models.CharField(max_length=25)
    time=models.CharField(max_length=25)

    def __unicode__(self):
        return  u"%s" %(self.message)