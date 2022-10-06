from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, "Articles/index.html", {
        "articles": articles
    })

def article(request, title):
    article = Article.objects.get(title=title)
    return render(request, "Articles/article.html", {
        "article": article
    })