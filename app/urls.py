from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # login user
    path("login/", views.LoginView.as_view(), name="login"),
    # create user
    url(r'^api/users/create/$', views.UserCreateView.as_view()), # create use
    # get user
    url(r'^api/user/$', views.GetUser.as_view()), # get user
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
