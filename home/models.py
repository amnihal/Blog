from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog")
    date = models.TimeField(auto_now_add=True) 




    def __str__(self) -> str:
        return self.title
