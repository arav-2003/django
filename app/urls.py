from django.urls import path
from . import views

urlpatterns=[
    path('',views.say, name='home'),
]