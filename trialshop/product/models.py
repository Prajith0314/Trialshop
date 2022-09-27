from django.db import models


class fashion_collection(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pic')
    price=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class comment_box(models.Model):
    fkey=models.ForeignKey(fashion_collection,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    msg=models.TextField()
    date=models.DateTimeField(auto_now_add=True)    

