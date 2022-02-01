from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from .views import UserProfileChangeAPIView
from django.conf.urls import url
from django.conf import settings
urlpatterns=[
# login user
path("login/", views.LoginView.as_view(), name="login"),
# create user
url(r'^api/users/create/$', views.UserCreateView.as_view()), # create user
# get user
url(r'^api/user/$', views.GetUser.as_view()), # get user
 path('api/profile/<username>',views.UserProfileChangeAPIView.as_view(),name='profile'),
 path('api/profile/', views.profilelist,name=''),
 path('api/createuser/', views.createuser,name=''),
 path('api/createrequest/', views.create_request,name=''),
 path('api/request/<request_id>', views.single_request,name=''),
 path('api/approve-request/<request_id>', views.approve_request,name=''),
 path('api/decline-request/<request_id>', views.decline_request,name=''),
 path('api/request/', views.all_requests,name=''),
 path('api/createasset/', views.create_asset,name=''),
 path('api/asset/<asset_id>', views.single_asset,name=''),
 path('api/asset/', views.all_assets,name=''),
 path('api/addstaff/', views.add_stafflist,name=''),
 path('api/deletestaff/<str:pk>/', views.deleteStaff,name='')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

