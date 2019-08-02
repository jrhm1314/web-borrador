from django.urls import path
from .views import InfoListView, InfoDetailView, FiltroListView
from . import views
info_patterns = ([
    path('', InfoListView.as_view(), name='list'),
    path('filtro/', FiltroListView.as_view(), name='filtro'),
    path('<int:pk>/', InfoDetailView.as_view(), name='detail'),
    path('filter/', views.publication_list, name='filter' ),
], "info")


#'<int:pk>/<slug:page_slug>/'   <username>/