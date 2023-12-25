from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    price = models.PositiveBigIntegerField()
    category = models.CharField(max_length=60, default='De uso geral')
    description = models.TextField(max_length=300)
    iva = models.IntegerField()
    image = models.ImageField(upload_to='')
    added = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'coala_shop_app_products'

class Shoppings(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Products_Likes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
