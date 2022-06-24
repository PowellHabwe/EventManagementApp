from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField(default = 0)
    header_image = models.ImageField(null=True, blank=True, upload_to='images')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})    

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)   

    


# class Products(models.Model):
#     name = models.CharField( max_length=1500) 
#     price = models.IntegerField(default = 0)

#     def __str__(self):
#         return self.name
        

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents

    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)        