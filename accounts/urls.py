from django.conf.urls import url
from django.contrib import admin


from .views import (UserCreateAPIView,UserLoginAPIView,userDetailsSerializer)

urlpatterns = [
    url(r'^register/$',UserCreateAPIView.as_view(),name='register'),
    url(r'^login/$',UserLoginAPIView.as_view(),name='login'),
    
]
