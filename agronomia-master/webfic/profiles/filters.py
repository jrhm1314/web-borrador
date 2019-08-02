from registration.models import Profile
import django_filters
from django import forms
from django.contrib.auth.forms import UserCreationForm





class ProfilesFilter(django_filters.FilterSet):
	nombre = django_filters.CharFilter(lookup_expr='icontains', label='Nombre')
	
	class Meta:
		model = Profile
		fields = ['nombre']
		