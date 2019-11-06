##default import
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

##model import
from .models import Post
from .models import imageTest

##form import
from homepage.forms import PostForm
from .forms import imageTestForm


##signup import
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
##from django.contrib.auth.forms import UserCreationForm  >>  장고의 기본 회원가입 폼 (ID, PW만 확인한다 - 뒤에서 이메일 추가 커스터미아징 예정)
from .forms import signupForm # 장고의 기본 회원가입 폼을 커스터마이징 한 폼
from django.urls import reverse


##User Views
# def signup(request):
#     url = "signup"
#     return render(request, 'homepage/user/signup.html', {'form': form, 'url': url})

# def signin(request):
#     url = "signin"
#     return render(request, 'homepage/user/signup.html', {'form': form, 'url': url})


# CBV (Class Based View 작성!)
class signupView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'homepage/user/signup.html' # 템플릿은?
    form_class =  signupForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    ##success_url = reverse('create_user_done') # 성공하면 어디로?

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?

##Test Views
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


def listTest(request):
    url = "listTest"
    posts = Post.objects.all()
    print(posts)
    return render(request, 'homepage/test/listTest.html', {'posts': posts, 'url': url})

def index(request):
    url = "index"
    return render(request, 'homepage/main/index.html', {'url':url})

def findSenior(request):
    url = "findSenior"
    return render(request, 'homepage/findSenior/findSenior.html', {'url':url})

def mapTest(request):
    url = "mapTest"
    return render(request, 'homepage/test/mapTest.html', {'url':url})

def imageTestView(request):
    if request.method == "GET":
        form = imageTestForm()
    elif request.method == "POST":
        form = imageTestForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'homepage/test/imageTest.html', ctx)


def detail(request, pk):
    image = imageTest.objects.get(pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=image.pk),
        '<p>주소는 {url}</p>'.format(url=image.image.url),
        '<p><img src="{url}" /></p>'.format(url=image.image.url),
    )
    return HttpResponse('\n'.join(messages))