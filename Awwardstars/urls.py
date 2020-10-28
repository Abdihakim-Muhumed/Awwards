from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('edit/',views.edit_profile,name='edit-profile'),
    path('my_profile/',views.profile,name='profile'),
]