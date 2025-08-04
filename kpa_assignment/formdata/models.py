# formdata/models.py

from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=255, unique=True)
    submittedBy = models.CharField(max_length=255)
    submittedDate = models.DateField()
    treadDiameterNew = models.CharField(max_length=255, null=True, blank=True)
    lastShopIssueSize = models.CharField(max_length=255, null=True, blank=True)
    condemningDia = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default='Saved')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.formNumber