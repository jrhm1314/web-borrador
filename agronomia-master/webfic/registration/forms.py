from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Publication, Estatus
from ckeditor.fields import RichTextField

class UserCreationFromWithEmail(UserCreationForm):
	email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("El email ya esta registrado, prueba con otro.")

		return email


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar', 'nombre', 'nombre_director', 'nombre_secretario', 'correo','telefono', 'enfoque_social', 'fecha_nac', 'direccion', 'pais', 'estado', 'ciudad', 'proyectos', 'miembros', 'objetivos', 'img_proyectos', 'img_miembros', 'img_objetivos']
		widgets = {
			'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'nombre': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Nombre de la organizacion'}),
			'nombre_director': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Nombre de director'}),
			'nombre_secretario': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Nombre de secretario'}),
			'telefono': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Telefono'}),
			'enfoque_social': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Enfoque social'}),
			'fecha_nac': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'fecha de creacion (ej. 03/03/2019)'}),
			'correo': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Correo de la organizacion'}),
			'direccion': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Direccion'}),
			'pais': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Pais'}),
			'estado': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Estado'}),
			'ciudad': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Ciudad'}),
			'proyectos': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Mensionar algunos proyectos'}),
			'miembros': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Describir sobre el perfil de los miembros'}),
			'objetivos': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'Objetivos de la organizacion'}),
			'img_proyectos': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3', 'placeholder':'Imagen que represente algun proyecto'}),
			'img_miembros': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'img_objetivos': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'})

		}



class PublicationForm(forms.ModelForm):
	class Meta:
		model = Publication
		fields = ['title', 'lugar', 'overview', 'fecha', 'hora','content', 'actividades', 'requisitos', 'logistica', 'maps', 'imagen', 'upload', 'estatus']
		widgets = {

			'title': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Titulo'}),
			'lugar': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Lugar'}),
			'overview': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Descripcion general, motivos del proyecto'}),
			'fecha': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':1, 'placeholder':'fecha de proyecto (ej. 03/03/2019)'}),
			'hora': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Hora'}),
			'content': forms.Textarea(attrs = {'class':'form-control'}),
			'actividades': forms.Textarea(attrs = {'class':'form-control'}),
			'requisitos': forms.Textarea(attrs = {'class':'form-control'}),
			'logistica': forms.Textarea(attrs = {'class':'form-control'}),
			'maps': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'(ej. https://www.google.com.mx/maps/dir/23.7437895,-99.1415427//@23.7434556,-99.1397939,17z/data=!4m2!4m1!3e0)'}),
			'imagen': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
			'upload': forms.ClearableFileInput(attrs = {'class':'form-control-file mt-3'})
		}

		labels = {

			'title':'','content': ''


		}


class EstatusForm(forms.ModelForm):
	class Meta:
		model = Estatus
		fields = ['status']






		


class EmailForm(forms.ModelForm):
	email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")
	class Meta:
		model = User
		fields = ['email']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if 'email' in self.changed_data:
			if User.objects.filter(email=email).exists():
				raise forms.ValidationError("El email ya esta registrado, prueba con otro.")

		return email
