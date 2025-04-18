from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    scam_type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    date_reported = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    evidence = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_reported'] 