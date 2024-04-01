from django.urls import path
from users.views import login_page, logout_page, sign_up_page, profile

urlpatterns = [
    path('Users/Login/', login_page, name='login_page'),
    path('Users/logout/', logout_page, name='logout_page'),
    path('Users/sign-up/', sign_up_page, name='sign_up'),
    path('Profile', profile, name='profile'),
]
