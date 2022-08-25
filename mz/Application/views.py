from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import TemplateView


def home_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'main_page.html', context)

def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_page.html', context)

class courses(TemplateView):
    template_name = 'courses.html'
    
    

