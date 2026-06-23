from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home),
    path('register',v.register),
    path('register2',v.register2),
    path('adduser',v.adduser),
    path('adduser2',v.adduser2),
    path('ulist',v.ulist),
]