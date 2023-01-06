from django.conf.urls import url



from .views import (PostListAPIView,PostDetailsAPIView,PostUpdateAPIView,PostCreateAPIView,PostDeleteAPIView)

urlpatterns = [
    url(r'^$',PostListAPIView.as_view(),name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailsAPIView.as_view(), name='detail'),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteAPIView.as_view(), name='delete'),



]
