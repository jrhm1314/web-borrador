from django.conf.urls import url
from django.urls import path
from .views import SignUpView, ProfileUpdate, PublicationUpdate, EmailUpdate, PerfilPageView, PublicationCreate, EstatusCreate, EstatusdosUpdate, EstatusListView, EstatusDeleteView, EsPubUpdate, PublicationDelete
from . import views

urlpatterns = [
	path('signup/', SignUpView.as_view(), name="signup"),
	path('profile/', ProfileUpdate.as_view(), name="profile"),
	path('perfil/', PerfilPageView.as_view(), name="perfil"),
	path('publication/update/<username>/<int:pk>/', PublicationUpdate.as_view(), name="publication"),
	path('publication/<username>/<int:pk>/', EsPubUpdate.as_view(), name="espub"),
	
	path('publication/create/', PublicationCreate.as_view(), name="publication_create"),
	path('publication/delete/<username>/<int:pk>/', PublicationDelete.as_view(), name='publication_delete'),
	path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
	path('estatus/create/', EstatusCreate.as_view(), name="estatus_create"),
	path('estatus/update/<int:pk>/', EstatusdosUpdate.as_view(), name="estatus_update"),
	path('estatus/list/', EstatusListView.as_view(), name='estatus_list'),
	path('estatus/delete/<int:pk>/', EstatusDeleteView.as_view(), name='estatus_delete'),
	
	
]