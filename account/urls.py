from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('my_account/', views.UserView.as_view(), name='my_account'),
]
