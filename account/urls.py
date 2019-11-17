from django.urls import path
from django.contrib.auth.decorators import login_required # dzięki temu przenosi nas do logowania jak nie jesteśmy zalogowani
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('my_account/', views.UserView.as_view(), name='my_account'),
    path('my_account/', login_required(views.UserView.as_view()), name='my_account'),

]
