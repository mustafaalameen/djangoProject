# from django.shortcuts import render
from django.views.generic import (TemplateView,
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView)
from .models import News, Comment
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    models= News
    template_name="news_reporter/home.html"
class NewsListView(ListView):
    model= News
    context_object_name= 'news'
    template_name= "news_reporter/news_home.html"

class NewsDetailsView(DetailView):
    model= News
    template_name= "news_reporter/news_detail.html"

class NewsCreateView(CreateView):
    model= News
    template_name= "news_reporter/news_create.html"
    fields= ['Headline','Reporter','Content']

class NewsUpdateView(UpdateView):
    model= News
    template_name= 'news_reporter/news_update.html'
    fields=['Headline','Content']

class NewsDeleteView(DeleteView):
    model= News
    template_name= 'news_reporter/news_delete.html'
    success_url= reverse_lazy('home')

class CommentView(CreateView):
    model= Comment
    template_name= 'news_reporter/news_comment.html'
    fields='__all__'
    success_url= reverse_lazy('news-home')
