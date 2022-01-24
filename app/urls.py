from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
urlpatterns=[
 path('api/profile/', views.profilelist,name=''),
 path('api/profile/<user_id>', views.singleprofile,name=''),
 path('api/createuser', views.createuser,name=''),


   

]