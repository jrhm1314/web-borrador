from .forms import UserCreationFromWithEmail, ProfileForm, EmailForm, PublicationForm, EstatusForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile, Publication, Estatus
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView

class StaffRequiredMixin(object):
    """ esten mixin reuqerira que el usuario sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
         return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)




@method_decorator(staff_member_required, name='dispatch')
class SignUpView(CreateView):
	form_class = UserCreationFromWithEmail
	success_url = reverse_lazy('profiles:filter')
	template_name = 'registration/signup.html'

	def get_success_url(self):
		return reverse_lazy('profiles:filter') + '?register'

	def get_form(self, form_class=None):
		form = super(SignUpView, self).get_form()
		#modificar en tiempo real
		form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder':'Nombre de usuario'})
		form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder':'Direccion de email'})
		form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Contraseña'})
		form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Repita la contraseña'})
		return form






@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
	form_class = ProfileForm
	success_url = reverse_lazy('perfil')
	template_name = 'registration/profile_form.html'

	

	def get_object(self):
		#recuperar el objeto que se va editar
		profile, created = Profile.objects.get_or_create(user=self.request.user)
		return profile






@method_decorator(login_required, name='dispatch')
class PublicationCreate(CreateView):
    form_class = PublicationForm
    success_url= reverse_lazy('publication_create')
    template_name = 'registration/publication.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PublicationUpdate(UpdateView):
	model = Publication
	form_class = PublicationForm
	success_url = reverse_lazy('info:filter')
	template_name = 'registration/publication.html'

	
	def get_object(self):
		return get_object_or_404(Publication, user__username=self.kwargs['username'], pk=self.kwargs['pk'])

@method_decorator(login_required, name='dispatch')
class PublicationDelete(DeleteView):
    model = Publication
    success_url = reverse_lazy('publication_create')


@method_decorator(login_required, name='dispatch')
class EsPubUpdate(UpdateView):
	model = Publication
	form_class = PublicationForm
	success_url = reverse_lazy('info:filter')
	template_name = 'registration/estatus.html'

	
	def get_object(self):
		return get_object_or_404(Publication, user__username=self.kwargs['username'], pk=self.kwargs['pk'])




@method_decorator(staff_member_required, name='dispatch')
class EstatusCreate(CreateView):
    form_class = EstatusForm
    success_url= reverse_lazy('estatus_list')
    template_name = 'registration/estatus.html'


@method_decorator(staff_member_required, name='dispatch')
class EstatusdosUpdate(UpdateView):
	model = Estatus
	form_class = EstatusForm
	success_url = reverse_lazy('estatus_list')
	template_name = 'registration/estatus.html'

	
	def get_object(self):
		return get_object_or_404(Estatus, pk=self.kwargs['pk'])


@method_decorator(staff_member_required, name='dispatch')
class EstatusListView(ListView):
    model = Estatus
    template_name = 'registration/estatus_list.html'
    paginate_by = 8

@method_decorator(staff_member_required, name='dispatch')
class EstatusDeleteView(DeleteView):
    model = Estatus
    success_url = reverse_lazy('estatus_list')



@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
	form_class = EmailForm
	success_url = reverse_lazy('profile')
	template_name = 'registration/profile_email_form.html'

	def get_object(self):
		#recuperar el objeto que se va editar
		return self.request.user

	def get_form(self, form_class=None):
		form = super(EmailUpdate, self).get_form()
		#modificar en tiempo real
		form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder':'Email'})
		return form

@method_decorator(login_required, name='dispatch')
class PerfilPageView(TemplateView):
	template_name = "registration/perfil.html"

	



