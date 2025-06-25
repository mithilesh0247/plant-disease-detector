from django.db import models

# Create your models here.
from django.db import models

class LeafImage(models.Model):
    image = models.ImageField(upload_to='leaf_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

