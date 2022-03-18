from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

class RaiseTicketForm(models.Model):
    ISSUE_STATUS = (('O','Open'),('C','Closed'))
    date = models.DateField(default=datetime.now)
    subject = models.CharField(max_length=200)
    issue = models.CharField(max_length=1900)
    status = models.CharField(max_length=7, choices=ISSUE_STATUS, default='O')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        db_table = 'tickets_raiseticketform'

