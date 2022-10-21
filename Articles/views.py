from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.

def article_titles():
    articles = Article.objects.all()
    titles = []
    for article in articles:
        titles.append(article.title) 
    return titles

def sort_articles():
    articles = Article.objects.all()
    articlesList = []
    for article in articles:
        articlesList.append(article)
    articlesList.sort(key=lambda article:article.date, reverse=True)
    return articlesList
    
def index(request):
    articles = sort_articles()
    return render(request, "Articles/index.html", {
        "articles": articles
    })

def article(request, title):
    article = Article.objects.get(title=title)
    return render(request, "Articles/article.html", {
        "article": article
    })

@login_required()
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        sources = request.POST["sources"]

        if not title or not content:
            return render(request, "Articles/create.html", {
                "message": "Incomplete Details."
            })

        a = Article(author=request.user,date=date.today(), title=title, content=content)
        a.save()

        if sources:
            sources = sources.split(",")

            for source in sources:
                s = Source(sourceURL=source)
                s.save()
                s.articles.add(a)
                s.save()
        return HttpResponseRedirect(reverse("Articles:index"))
    return render(request, "Articles/create.html")


def edit(request, title):
    article = Article.objects.get(title=title)
    if request.method == "POST":
        title = request.POST["title"]

        titles = article_titles()
        titles.remove(article.title)
        if title in titles:
            return render(request, "Articles/edit.html", {
                "article": article,
                "message": "Title Already Taken."
            })
        content = request.POST["content"]
        article.content = content
        article.title = title
        article.save()
        return HttpResponseRedirect(reverse("Articles:article", args=(article.title,)))
    return render(request, "Articles/edit.html", {
        "article": article
    })
    

def delete(request, title):
    Article.objects.filter(title=title).delete()
    sources = Source.objects.all()
    for source in sources:
        if source.title == "" and len(source.articles.all()) == 0:
            source.delete()
    return HttpResponseRedirect(reverse("Articles:index"))