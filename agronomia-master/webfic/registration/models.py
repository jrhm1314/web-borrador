from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

# Create your models here.
def custom_upload_to(instance, filename):
	old_instance = Profile.objects.get(pk=instance.pk)
	old_instance.avatar.delete()
	return 'profiles/' + filename

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
	telefono = models.CharField(null=True, blank=True, max_length=10) 
	nombre = models.CharField(null=True, blank=True, max_length=40)
	nombre_director = models.CharField(null=True, blank=True, max_length=40)
	nombre_secretario = models.CharField(null=True, blank=True, max_length=40)
	enfoque_social = models.CharField(null=True, blank=True, max_length=50)
	fecha_nac = models.DateField(null=True, auto_now_add=False, verbose_name="fecha de creación de la organizacion (ej. 03/03/2019)")
	correo = models.CharField(null=True, blank=True, max_length=100)
	direccion = models.CharField(null=True, blank=True, max_length=100)
	pais = models.CharField(null=True, blank=True, max_length=50)
	estado = models.CharField(null=True, blank=True, max_length=50)
	ciudad = models.CharField(null=True, blank=True, max_length=50)
	proyectos = models.CharField(null=True, blank=True, max_length=400)
	miembros = models.CharField(null=True, blank=True, max_length=400)
	objetivos = models.CharField(null=True, blank=True, max_length=400)
	img_proyectos = models.ImageField(upload_to='experiencia', null=True, blank=True)
	img_miembros = models.ImageField(upload_to='educacion', null=True, blank=True)
	img_objetivos = models.ImageField(upload_to='habilidades', null=True, blank=True)

	class Meta:
		ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
	if kwargs.get('created', False):
		Profile.objects.get_or_create(user=instance)
		print("se ha creado un usuario y su perfil")



class Estatus(models.Model):
	status = models.CharField(null=True, blank=True, max_length=100)
	#publication = models.ForeignKey(Publication, null=True, blank=True, on_delete=models.CASCADE)  
	#status = models.CharField(max_length=15, choices=status_op, default='Espera')

	def __str__(self):
		return self.status
	

class Publication(models.Model):
	user =  models.ForeignKey(User, verbose_name="Nombre de usuario", on_delete=models.CASCADE)
	title = models.CharField(null=True, blank=True, verbose_name="Título", max_length=100)
	lugar = models.CharField(null=True, blank=True, verbose_name="Lugar", max_length=100)
	overview = models.CharField(null=True, blank=True, verbose_name="Motivo", max_length=100)
	fecha = models.DateField(null=True, auto_now_add=False, verbose_name="fecha de proyecto (ej. 03/03/2019)")
	hora = models.CharField(null=True, blank=True, verbose_name="Hora", max_length=10)
	content = RichTextField(null=True, blank=True, verbose_name="Contenido")
	actividades = RichTextField(null=True, blank=True, verbose_name="Actividades")
	requisitos = RichTextField(null=True, blank=True, verbose_name="Requisitos")
	logistica = RichTextField(null=True, blank=True, verbose_name="Logistica")
	maps = models.CharField(null=True, blank=True, verbose_name="maps", max_length=200)
	imagen = models.ImageField(upload_to='Publications', null=True, blank=True, verbose_name="Imagen principal")
	upload = models.FileField(null=True, blank=True, upload_to='uploads/', verbose_name="Documento")
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
	estatus = models.ForeignKey(Estatus, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Categoria")
  	


	class Meta:
		ordering = ['-created']
