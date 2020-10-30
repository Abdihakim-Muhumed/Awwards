from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('edit/',views.edit_profile,name='edit-profile'),
    path('my_profile/',views.profile,name='profile'),
    path('new/project/',views.new_project,name='new-project'),
    path(r'project/view/(\d<project_id>+)',views.view_project,name='view-project'),
    path(r'ajax/rate/(\d<project_id>+)', views.rate_project,name='rate-project'),
    path('projects/search/',views.search_results,name='search'),
]

