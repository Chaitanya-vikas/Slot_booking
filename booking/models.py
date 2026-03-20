from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone # Make sure this is imported!

class Slot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    customer_name = models.CharField(max_length=100, blank=True, null=True)

    #To check if the slot is in the past
    @property
    def is_completed(self):
        now = timezone.localtime()
        # If the date is strictly in the past
        if self.date < now.date():
            return True
        # If the date is today, but the end time has already passed
        if self.date == now.date() and self.end_time < now.time():
            return True
        return False

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError("A slot must end on the same day. End time cannot be earlier than or equal to start time.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} | {self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"