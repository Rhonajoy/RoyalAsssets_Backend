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
 path('api/request/<request_id>', views.single_request,name=''),
 path('api/request/', views.all_requests,name=''),
 path('api/createasset/', views.create_asset,name=''),
 path('api/asset/<asset_id>', views.single_asset,name=''),
 path('api/asset/', views.all_assets,name=''),







]




   

