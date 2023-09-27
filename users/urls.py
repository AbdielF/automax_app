from django.urls import path
from .views import users_view_login, UsersViewRegister, users_view_logout, UsersViewProfile


urlpatterns = [
    path('login/', users_view_login, name='login'),
    path('register/', UsersViewRegister.as_view(), name='register'),
    path('logout/', users_view_logout, name='logout'),
    path('profile/', UsersViewProfile.as_view(), name='profile')
]