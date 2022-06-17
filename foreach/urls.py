from django.urls import path
from .views import index,create_comment,delete_comment
from django.conf.urls import handler404
from .views import error404
urlpatterns=[
    path('',index),
    path('newComment/',create_comment, name='create_comment'),
    path('delete_comment/<int:comment_id>/',delete_comment, name='delete_comment')
]
handler404 = error404