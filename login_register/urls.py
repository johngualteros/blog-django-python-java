from django.urls import path
from .views import register,login,create_user
from django.conf.urls import handler404
from foreach.views import error404
urlpatterns=[
    path('register/',register, name='register'),
    path('register/create_user', create_user, name='create_user'),
    path('login/',login,name="login")
]
handler404 = error404