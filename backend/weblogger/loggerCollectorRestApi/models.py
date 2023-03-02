from django.db import models

# Create your models here.

class Device(models.Model):

    #ip address
    ipaddress = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.ipaddress}"


class Log(models.Model):

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    types = models.CharField(max_length=100)
    datetime = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f"{self.device.ipaddress} {self.content}"
    
    class Meta:
        ordering = ['-datetime']
