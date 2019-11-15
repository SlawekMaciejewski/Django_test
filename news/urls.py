from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('list/', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('author/', views.author, name='author'),
]
