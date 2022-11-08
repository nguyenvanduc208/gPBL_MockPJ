from django.db import models
from uuid import uuid4
from category.models import Category
from image.models import Image
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=12,decimal_places=3)
    image = models.ForeignKey(to=Image, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)