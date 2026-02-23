from django.urls import path
from . import views
urlpatterns = {
    path('', views.home, name='home'),
    path('/bug', views.bug, name-"bug")
}