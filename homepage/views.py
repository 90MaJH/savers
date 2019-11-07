##default import
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

##model import
from .models import Post

##form import
from homepage.forms import PostForm


##findSenior Views
def findSenior(request):
    url = "findSenior"
    return render(request, 'homepage/findSenior/findSenior.html', {'url':url})

##chatting Views
def chattingListView(request):
    url = "chattingList"
    return render(request, 'homepage/chatting/chattingList.html', {'url':url})

def chattingView(request):
    url = "chattingList"
    return render(request, 'homepage/chatting/chatting.html', {'url':url})


## test views
def test(request):
    url = "test"
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
        return render(request, 'homepage/test/test.html', {'form': form, 'url': url})

def listTest(request):
    url = "listTest"
    posts = Post.objects.all()
    print(posts)
    return render(request, 'homepage/test/listTest.html', {'posts': posts, 'url': url})

def index(request):
    url = "index"
    return render(request, 'homepage/main/index.html', {'url':url})



def mapTest(request):
    url = "mapTest"
    return render(request, 'homepage/test/mapTest.html', {'url':url})
