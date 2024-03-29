##default import
from django.forms import ModelForm
from django import forms

##summernote import
from django_summernote.widgets import SummernoteWidget

##model import
from .models import Post
from .models import imageTest

##signup import
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


##user models
# class signupForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
#     email = forms.EmailField(required=True) # 이메일 필드 추가
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True): # 저장하는 부분 오버라이딩
#         user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user


# class signinForm(forms.ModelForm):



##Test Models




##test form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }

class imageTestForm(forms.ModelForm):
    class Meta:
        model = imageTest
        fields = ('image', 'content',)
