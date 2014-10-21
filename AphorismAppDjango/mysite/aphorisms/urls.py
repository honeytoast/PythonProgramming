#### Grace Hadiyanto
#### e-mail: ifoundparis@gmail.com
#### Assignment 7
#### CS223P

from django.conf.urls import patterns, url

from aphorisms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
