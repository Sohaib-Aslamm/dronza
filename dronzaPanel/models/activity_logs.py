from django.db import models
from django.utils.timezone import now


class ActivityLog(models.Model):
    django_view = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    stack_trace = models.TextField(null=True, blank=True)
    user_ip = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = 'Activity Logs'
