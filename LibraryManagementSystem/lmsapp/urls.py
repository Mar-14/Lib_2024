from django.urls import path
from .views import add_books, custom_logout, index,register, user_login

urlpatterns=[

    path('',index,name='home_path'),
    path('useraccount/register/',register,name='register'),
    path('accounts/login/',user_login,name='login'),
    path('logout/',custom_logout, name="logout"),
    path('add_books/',add_books, name='add_books'),
]