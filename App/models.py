from django.db import models
from django.utils.text import slugify


class Video(models.Model):
    v_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default="")
    rating = models.CharField(max_length=100, default="")
    file = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title
    
    
class Article(models.Model):
    a_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default="")
    rating = models.CharField(max_length=100, default="")
    content = models.TextField(max_length=5000, default="")
    image = models.ImageField() 
    
    def __str__(self):
        return self.title  
    
    
class Hotel(models.Model):
    hotel_id = models.IntegerField(default=0)
    hotel_title = models.CharField(max_length=100, default="")
    discription = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=10, default="")
    rating = models.CharField(max_length=20, default="")
    image = models.ImageField()
    hotel_title1 = models.CharField(max_length=100, default="", blank=True)
    hotel_desc1 = models.CharField(max_length=100, default="", blank=True)
    hotel_price1 = models.CharField(max_length=10, default="", blank=True)
    hotel_rating1 = models.CharField(max_length=10, default="", blank=True)
    hotel_image1 = models.ImageField(blank=True)
    reviews1 = models.CharField(max_length=10, default="", blank=True)
    comfort1 = models.CharField(max_length=10, default="", blank=True)
    cleanliness1 = models.CharField(max_length=10, default="", blank=True)
    value_for_money1 = models.CharField(max_length=10, default="", blank=True)
    facilities1 = models.CharField(max_length=10, default="", blank=True)
    hotel_title2 = models.CharField(max_length=100, default="", blank=True)
    hotel_desc2 = models.CharField(max_length=100, default="", blank=True)
    hotel_price2 = models.CharField(max_length=10, default="", blank=True)
    hotel_rating2 = models.CharField(max_length=10, default="", blank=True)
    hotel_image2 = models.ImageField(blank=True)
    reviews2 = models.CharField(max_length=10, default="", blank=True)
    comfort2 = models.CharField(max_length=10, default="", blank=True)
    cleanliness2 = models.CharField(max_length=10, default="", blank=True)
    value_for_money2 = models.CharField(max_length=10, default="", blank=True)
    facilities2 = models.CharField(max_length=10, default="", blank=True)
    
    def __str__(self):
        return self.hotel_title
    
     
class Place(models.Model):
    place_id = models.IntegerField(default=0)
    place_title = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=10, default="")
    rating = models.CharField(max_length=20, default="")
    image = models.ImageField()
    image_url = models.URLField(default="")

    def __str__(self):
        return self.place_title
    
    
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    firstName= models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    massage= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.firstName