from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('' , views.PostView.as_view(), name='home'),
    path('details/<slug:slug>' , views.DetailView.as_view() , name='details'),
    path('like/<slug:slug>/<int:pk>' , views.like , name='like'),
]