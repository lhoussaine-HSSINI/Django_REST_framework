from django.db import models
from  datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=15)
    content = models.TextField()
    image=models.ImageField(upload_to='fotoyat/%y/%m/%d')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Product'
        ordering=['name']

class Test(models.Model):
    date = models.DateField()
    time=models.TimeField(null=True)
    created=models.DateTimeField(default=datetime.now())