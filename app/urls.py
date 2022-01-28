from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from .views import UserProfileChangeAPIView

urlpatterns=[
 path('api/profile/<username>',views.UserProfileChangeAPIView.as_view(),name='profile'),
 path('api/profile/', views.profilelist,name=''),
 path('api/createuser/', views.createuser,name=''),
 path('api/createrequest/', views.create_request,name=''),
 path('api/createuser/', views.createuser,name=''),
 path('api/createuser/', views.createuser,name=''),
 path('api/createasset/', views.create_asset,name=''),
 path('api/createuser/', views.createuser,name=''), 
 path('api/createuser/', views.createuser,name=''),







]




   

