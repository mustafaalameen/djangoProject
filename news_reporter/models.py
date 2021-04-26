from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

class News(models.Model):
    Headline=models.CharField(max_length=400)
    Reporter=models.ForeignKey('auth.User', on_delete = models.CASCADE)
    Content=models.TextField()
    Date_reported=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.Headline[:50])

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])
    

class Comment(models.Model):
    news=models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    comment=models.CharField(max_length=255)
    name= models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s-%s' % (self.news.Headline, self.name)

    