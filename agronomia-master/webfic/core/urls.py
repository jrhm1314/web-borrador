from django.urls import path
from .views import HomePageView, SamplePageView,  MainPageView, PubListView, my_view
from . import views

urlpatterns = [
    path('', PubListView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('main/', MainPageView.as_view(), name="main"),
    path('pub', PubListView.as_view(), name="pub_list"),
    path('myview', views.my_view, name="myview"),
    
]


