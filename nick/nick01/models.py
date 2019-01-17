import django
from django.db import models
IS_DELETED = (
     (True, True),
     (False, False),
)

ROLE_STATUS = (
     ('Active', 'Active'),
     ('Inactive', 'Inactive'),
)
class State(models.Model):
     state = models.CharField(max_length=500, blank=True)
     created_by = models.CharField(max_length=50, blank=False, null=False)
     updated_by = models.CharField(max_length=50, blank=True, null=True)
     created_on = models.DateTimeField(default=django.utils.timezone.now)
     updated_on = models.DateTimeField(blank=True, null=True)
     is_deleted = models.BooleanField(choices=IS_DELETED, default=False)

     def __unicode__(self):
         return unicode(self.state)


class City(models.Model):
    city = models.CharField(max_length= 500,blank=False)
    pincode = models.IntegerField (max_length= 30,blank=False)
    division = models.CharField(max_length=100,blank=False)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(default=django.utils.timezone.now)
    state1 = models.ForeignKey(State, blank=True,null= True)

    def __unicode__(self):
        return unicode(self.city)


class Home(models.Model):
    Ownername = models.CharField(max_length= 500,blank=False)
    homeNO = models.IntegerField (max_length= 30,blank=False)
    street = models.CharField(max_length=100,blank=False)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(default=django.utils.timezone.now)
    city1 = models.ForeignKey(City, blank=True,null= True)

    def __unicode__(self):
        return unicode(self.homeNO)


