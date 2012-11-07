from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.user.username

    def get_bids(self):
	pass
 
    def get_reputation(self):
        pass

class Project(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_add_now = True)
    modified_on = models.DateTimeField(auto_add = True)

    def __unicode__(self):
        return self.name

    def get_bids(self):
        pass

    def get_likes(self):
        pass

class Bid(models.Model):
    project = models.ForeignKey(User)
    bidder = models.ForeignKey(Project)
    bid_on = models.DateTimeField(auto_add_now=True)
    modified_on = models.DateTimeField(auto_add)
    price = models.PositiveIntegerField()
    payment_type = models.CharField(max_length=10,choices=((u'strict',u'Strict'),(u'negotiable',u'Negotiable')))
    deliver_date = models.DateTimeField()
    is_winner = models.BooleanField(default=False)

    def __unicode__(self):
        return self.project.name

class Like(self):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    is_null = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_add_now = True)
    modified_on = models.DateTimeField(auto_add = True)

    def __unicode__(self):
        return project.name
