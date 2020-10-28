from django.conf.urls import url
from . import views
from django_re
urlpatterns = [
    url('',views.index, name='index'),
]