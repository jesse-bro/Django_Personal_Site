from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('contact/', views.contact, name='contact'),
    url('projects/', views.projects, name='projects'),
    url('education/', views.education, name='education'),
]