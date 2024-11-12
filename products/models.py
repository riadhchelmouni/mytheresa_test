from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    price = models.IntegerField(help_text="Price in cents")  # Price is stored as an integer in cents

    def __str__(self):
        return self.name
