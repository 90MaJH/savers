##default import
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

##model import
from .models import Post
from .models import User

##form import
from homepage.forms import PostForm


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
        return render(request, 'homepage/test/test.html', {'form': form, 'url': url})

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
