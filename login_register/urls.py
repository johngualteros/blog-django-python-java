from django.urls import path
from .views import register,login
from django.conf.urls import handler404
from foreach.views import error404
urlpatterns=[
    path('register/',register, name='register'),
    path('login/',login,name="login")
]
handler404 = error404