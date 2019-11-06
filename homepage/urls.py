from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.index, name='defaultIndex'),
    path('index', views.index, name='index'),
    path('findSenior', views.findSenior, name='findSenior'),
    path('test', views.test, name='test'),
    path('listTest', views.listTest, name='listTest'),
    path('mapTest', views.mapTest, name='mapTest'),
    path(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    path('imageTest', views.imageTestView, name='imageTest'),
    path('signup', views.signupView, name='signup'),
    # path('signin', views.signin, name='signin'),
]

urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
