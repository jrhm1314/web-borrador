from registration.models import Publication
import django_filters





class PublicationFilter(django_filters.FilterSet):
	user__username = django_filters.CharFilter(lookup_expr='icontains', label='Nombre de usuario')
	title = django_filters.CharFilter(lookup_expr='icontains', label='Titulo')
	

	class Meta:
		model = Publication
		fields = [
		'user__username', 'title', 'estatus',
		]
		
		
