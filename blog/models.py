
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    #image=models.ImageField(upload_to='media/blog/',default='blog/defult.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    content= models.TextField()
    #tags=TaggableManager()
    #category=models.ManyToManyField(category)
    count_views= models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    #login_require= models.BooleanField(default=False)
    publish_date= models.DateTimeField(null=True)
    create_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)

    class Meta :
        ordering=['create_date']
    def __str__(self):
        return "title{} and Id{}".format(self.title,self.ID)
        #return '%d'%self.id

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)