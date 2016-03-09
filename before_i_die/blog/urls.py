from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^home/$', views.UserPosts.as_view(), name='home'),
    url(r'^create_post/$', views.CreatePost.as_view(), name='create_post'),
    url(r'^post_detail/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^add_like/(?P<pk>\d+)/$', views.CreateLike.as_view(), name='add_like'),
    url(r'^dislike/(?P<pk>d\+)/$', views.Dislike.as_view(), name='dislike'),
    url(r'^users/$', views.ActiveUsers.as_view(), name='users'),
    url(r'^user_posts/(?P<pk>\d+)/$', views.UserPostDetail.as_view(), name='user_posts'),
    url(r'^search/$', views.TagSearch.as_view(), name='search'),
]
