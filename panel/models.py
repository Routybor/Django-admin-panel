from django.db import models

class Computer(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cpu = models.CharField(max_length=255, blank=True, null=True)
    gpu = models.CharField(max_length=255, blank=True, null=True)
    ram = models.CharField(max_length=255, blank=True, null=True)
    motherboard = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.BinaryField(blank=True, null=True, editable=True)

    def __str__(self):
        return self.title
