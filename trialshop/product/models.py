from django.db import models

class fashion_collection(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pic')
    price=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

