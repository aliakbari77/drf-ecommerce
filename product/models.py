from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Attribute(models.Model):
    name = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)


class AttributeValue(models.Model):
    value = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attribute_value')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=6)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_line')


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.FileField(upload_to='media/images/')
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE, related_name='product_image')
