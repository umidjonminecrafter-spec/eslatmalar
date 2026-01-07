from django.db import models

# Create your models here.
class Eslatmalar(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Kartochka(models.Model):
    sarlavha = models.CharField(max_length=100)
    izoh = models.CharField(max_length=100)
    def __str__(self):
        return self.sarlavha