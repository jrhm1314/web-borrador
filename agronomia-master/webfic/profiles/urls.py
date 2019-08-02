from django.urls import path
from .views import ProfileListView, ProfileDetailView
from . import views

profiles_patterns = ([
	path('filter/', views.profile_list, name='filter'),
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),

], "profiles")
