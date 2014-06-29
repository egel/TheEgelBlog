from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.


class SingUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    timestamp = models.DataTimeField()
    updated = models.DataTimeField()

    def __unicode__(self):
        return smart_unicode(self.email)
