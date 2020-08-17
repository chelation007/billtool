from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100,unique=True)
    hsn_nbr = models.CharField(max_length=30)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    rate = models.IntegerField()
    mrp = models.IntegerField()
    total_stock = models.IntegerField()


    def __str__(self):
        return '%s' % (self.name)
