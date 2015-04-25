from django.db import models
import os

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='icons',blank=True,null=True)

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

class Image(models.Model):
    def get_pictures_path(instance,filename):
        return os.path.join('pictures', str(instance.pk), filename)
    product = models.ForeignKey(Product)
    picture = models.ImageField(upload_to=get_pictures_path, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return "Foto de " + self.product.name
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.picture
            self.picture = None
            super(Image, self).save(*args, **kwargs)
            self.picture = saved_image

        super(Image, self).save(*args, **kwargs)