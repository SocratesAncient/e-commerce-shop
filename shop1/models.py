from django.db import models
from django.db.models.base import ModelState, ModelStateFieldsCacheDescriptor
from django.db.models.fields import SlugField
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug=models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product_list_by_category',args=[self.slug])

class Product(models.Model):
    category=models.ForeignKey('Category',
    related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200, db_index=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d',
    blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('product_detail',args=[self.id,self.slug])