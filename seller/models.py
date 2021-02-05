from django.db import models


# Create your models here.
class Sellpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='seller/images', default="")

    def __str__(self):
        return self.product_name


