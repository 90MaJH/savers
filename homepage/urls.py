from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


from . import views
from homepage.views import *

urlpatterns = [
    path('', views.index, name='defaultIndex'),
    path('index', views.index, name='index'),
    path('findSenior', views.findSenior, name='findSenior'),
    path('chatting', views.chattingView, name='chatting'),
    path('profile', views.profileView, name='profile'),


    ##user urls
    path('signup_test', user_register_page_test, name='registerTest'),
    path('user_register_test/', user_register_page_test, name='registerTest'),
    path('homepage/user_register_idcheck_test/', user_register_idcheck_test, name='registeridcheckTest'),
    path('user_register_res_test/', user_register_result_test, name='registerresTest'),
    path('user_register_completed_test/', user_register_completed_test, name='registercompletedTest'),
    path('login_test/', auth_views.LoginView.as_view(template_name='homepage/test/login_test.html'), name='loginTest'),
    path('logout_test/', auth_views.LogoutView.as_view(), name='logoutTest'),



    ##test urls
    path('chattingList', views.chattingListView, name='chattingList'),
    path('test', views.test, name='test'),
    path('listTest', views.listTest, name='listTest'),
    path('mapTest', views.mapTest, name='mapTest'),
    path(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    path('imageTest', views.imageTestView, name='imageTest'),
    path('signup', views.signupView, name='signup'),
    # path('signin', views.signin, name='signin'),
]

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
