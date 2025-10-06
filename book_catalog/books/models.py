from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    pages = models.PositiveIntegerField()
    cover_image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title
    
    

