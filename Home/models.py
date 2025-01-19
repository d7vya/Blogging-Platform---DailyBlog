from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name=models.CharField('Category name', max_length=50,primary_key=True)
    slug_cat=models.CharField( max_length=50,blank=True)
    def save(self, *args, **kwargs):
        if not self.slug_cat:
            self.slug_cat = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self) :
        return self.name      


class Tag(models.Model):
    name= models.CharField('Tag Name', max_length=100,primary_key=True)
    tag_slug=models.CharField( max_length=50,blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.tag_slug:
            self.tag_slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self) :
        return self.name   

    
class Blog(models.Model):
    username= models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)    
    title=models.CharField('blog title', max_length=100)
    desc=models.CharField('Blog description', max_length=300)
    body=models.TextField('Blog body')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,to_field='name')
    tags= models.ManyToManyField(Tag)
    datentime=models.DateTimeField('Date and Time ',  auto_now_add=True,auto_now=False)
    update=models.DateTimeField('update on', auto_now=True,auto_now_add=False)
    view_count= models.IntegerField('Total Views',default=0)
    commen_count= models.IntegerField('Total Commentss',default=0)
    def __str__(self) :
        return self.title  
    
class Comment(models.Model):
    blog= models.ForeignKey(Blog, verbose_name='Blog Title', on_delete=models.CASCADE)    
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField('comment', max_length=150)
    datentime=models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self) :
        return self.content  