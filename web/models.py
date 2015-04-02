from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = "sub categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    subcategory= models.ForeignKey(SubCategory,null=True)

    def on_sale(self):
        return self.discount>0

    def __str__(self):
        return self.name