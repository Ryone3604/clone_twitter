from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post_new/', views.PostCreateView.as_view(), name='post-create'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('setting/(?P<pk>[0-9]+)/$', views.ProSettingV.as_view(), name='pro_setting'),
    path('setting/', views.ProSettingVV.as_view(), name='pro_setting3'),
    
]
