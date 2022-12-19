from django.urls import path
from . import views
from .views import AllSaveView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SaveView, UserPostListView, LikeView,LikeCommentView, posts_of_following_profiles,  AllLikeView
from django.urls.resolvers import URLPattern
from .views import cancel_friend_request, decline_friend_request, friend_requests, friends_list_view, remove_friend, send_friend_request, accept_friend_request
from .views import ShowNotifications



urlpatterns = [
    path('list/<user_id>', friends_list_view, name='list'),
    path('friend_request/', send_friend_request, name="friend-request"),
    path('friend_requests/<user_id>/', friend_requests, name='friend-requests'),
    path('friend_request_accept/<friend_request_id>/', accept_friend_request, name='friend-request-accept'),
    path('friend_remove/', remove_friend, name='remove-friend'),
    path('friend_request_decline/<friend_request_id>/', decline_friend_request, name='friend-request-decline'),
    path('friend_request_cancel/', cancel_friend_request, name='friend-request-cancel'),
    path('', views.first, name='firsthome'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('feed/', posts_of_following_profiles, name='posts-follow-view'),
    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/like/', LikeView, name='post-like'),
    path('liked-posts/', AllLikeView, name='all-like'),
    path('post/save/', SaveView, name='post-save'),
    path('saved-posts/', AllSaveView, name='all-save'),
    path('post/comment/like/', LikeCommentView, name='comment-like'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search, name='search'),
    path('', ShowNotifications, name='show-notifications'),
    path('all/', views.ProfileListView.as_view(), name='profile-list-view'),
    path('follow/', views.follow_unfollow_profile, name='follow-unfollow-view'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
    path('public-profile/<str:username>/', views.public_profile, name='public-profile'),
    
    
]