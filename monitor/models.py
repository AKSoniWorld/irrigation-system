from django.db import models

MODE_CHOICES = (
    ('automated', 'Automated'),
    ('manual', 'Manual'),
)
class DeviceState(models.Model):
    moisture = models.IntegerField()
    status = models.BooleanField()
    time = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return "Device => M:" + str(self.moisture) + " S:" + str(self.status)


class DeviceControl(models.Model):
    set_state = models.BooleanField()
    lower_threshold = models.IntegerField(default=15)
    upper_threshold = models.IntegerField(default=50)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='automated')  # 0=Automated, 1=Manual

    def __str__(self):
        if self.set_state:
            return "Device ON"
        else:
            return "Device OFF"
