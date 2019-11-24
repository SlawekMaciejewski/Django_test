from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='list_post'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/<str:name>/<str:email>/<str:content>/addcomment/',
         views.AddCommentView.as_view(), name='addcomment')
]