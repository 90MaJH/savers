##default import
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

##model import
from .models import Post
from .models import User, imageTest
from .models import

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


##user Views
def user_register_page_test(request):
    return render(request, 'homepage/test/user_register_test.html')

def user_register_idcheck_test(request):
    if request.method == "POST":
        username = request.POST['username']
    else:
        username = ''

    print(User.objects.all())
    idObject = User.objects.filter(username__exact=username)
    idCount = idObject.count()

    if idCount > 0:
        msg = "<font color='red'> the id is alerady exist.</font>"
        msg += "<input type='hidden' name='IDCheckResult' id='IDCheckResult' value=0 />"
    else:
        msg = "<font color='blue'> the id is avaiable.</font>"
        msg += "<input type='hidden' name='IDCheckResult' id='IDCheckResult' value=1 />"

    return HttpResponse(msg)


def user_register_result_test(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        last_name = request.POST['last_name']
        # phone = request.POST['phone']
        phone = '01012431234'
        # email = request.POST['email']
        email = 'test1@test1.com'
        birth_year = request.POST['birth_year']
        birth_month = request.POST['birth_month']
        birth_day = request.POST['birth_day']

    try:
        if username and User.objects.filter(username__exact=username).count() == 0 :
            # date_of_birth = datetime(birth_year, birth_month, birth_day)
            user = User.objects.create_user(
                username,password,last_name, email, phone, '1990-01-01'
            )

            redirection_page = 'user_register_completed/'

        else:
            redirection_page = 'error'
    except Exception as ex:
        print('error occured :', ex)

    return redirect(redirection_page)


def user_register_completed_test(request):
    return render(request, 'homepage/test/user_register_completed_test.html')


##findSenior Views
def findSenior(request):
    url = "findSenior"
    return render(request, 'homepage/findSenior/findSenior.html', {'url':url})

##chatting Views
def chattingListView(request):
    url = "chattingList"
    return render(request, 'homepage/chatting/chattingList.html', {'url':url})

def chattingView(request):
    url = "chatting"
    return render(request, 'homepage/chatting/chatting.html', {'url':url})

##profile Views
def profileView(request):
    url = "profile"
    return render(request, 'homepage/profile/profile.html', {'url':url})


## test views
def test(request):
    url = "test"
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = Post(title=form['title'].value(), content=form['content'].value())
            obj.save()
            return HttpResponse("success")
        return("fail")
    elif request.method == 'GET':
        form = PostForm()

def listTest(request):
    url = "listTest"
    posts = Post.objects.all()
    return render(request, 'homepage/test/listTest.html', {'posts': posts, 'url': url})

def index(request):
    url = "index"
    return render(request, 'homepage/main/index.html', {'url':url})



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