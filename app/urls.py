from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
urlpatterns=[
 path('api/profile/', views.profilelist.as_view(),name=''),
 path('api/profile/<str:username>', views.singleprofile.as_view(),name=''),

   

]