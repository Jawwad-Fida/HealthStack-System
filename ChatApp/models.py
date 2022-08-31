from django.db import models
from hospital.models import User
from django.utils import timezone
# Create your models here.
class chatMessages(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.message