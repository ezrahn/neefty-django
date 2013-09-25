from django.db import models, connection
from django.conf import settings
from django.contrib.auth.models import User


#class User(DjangoUser):

#    def __str__(self):
#        return self.getFullName()

#    def getFullName(self):
#        full_name = ''
#        if self.first_name or self.last_name:
#            full_name = self.first_name + ' ' + self.last_name
#        else:
#            full_name = self.email
#        return full_name.strip()
#    full_name = property(getFullName)

class Dimension(models.Model):
    name = models.CharField(max_length=80, null=False)
    user = models.ForeignKey(User, related_name='dimensions')


class ListItem(models.Model):
    name = models.CharField(max_length=80, null=False)
    dimension = models.ForeignKey(Dimension, related_name="list_items")
    