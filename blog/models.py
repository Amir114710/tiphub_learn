from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    conttent = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post , self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:details' , kwargs={'slug':self.slug})
        
class Like(models.Model):
    users = models.ForeignKey(User, related_name='likes' , on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, related_name='likes' , on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.users.email} - {self.posts.title}"

        
