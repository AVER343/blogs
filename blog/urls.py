
from django.urls import path
from . import views
from .views import UserPostListView,PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
urlpatterns = [
    path('',PostListView.as_view(), name='app-21'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('about/',views.about,name='app-home'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]


