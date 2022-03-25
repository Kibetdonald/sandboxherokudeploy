from django.db import models

# Create your models here.


class Products(models.Model):
    prd_title = models.CharField(max_length=200)
    prd_cat = models.CharField(max_length=100)
    prd_price = models.IntegerField()
    prd_desc = models.TextField()
    prd_img = models.ImageField(upload_to='pics')
    prd_keyword = models.CharField(max_length=100, null=True,)
    prd_quantity = models.IntegerField(default=0)
