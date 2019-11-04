##default import
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

##model import
from .models import Post

##form import
from homepage.forms import PostForm


def test(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = Post(title=form['title'].value(), content=form['content'].value())
            print("############")
            print(Post)
            print(obj)
            obj.save()
            return HttpResponse("success")
        return("fail")
    elif request.method == 'GET':
        form = PostForm()
        return render(request, 'homepage/test/test.html', {'form': form})


def listTest(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'homepage/test/listTest.html', {'posts': posts})

def index(request):
    return render(request, 'homepage/main/index.html', {})

def findSenior(request):
    return render(request, 'homepage/findSenior/findSenior.html', {})
