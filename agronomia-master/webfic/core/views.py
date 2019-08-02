from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from django.urls import reverse_lazy
from registration.models import Publication, Profile
from django.views.generic.list import ListView

from django.http import HttpResponse
from django.template import RequestContext, loader


class HomePageView(TemplateView):
	template_name = "core/home.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'title':"SISTEMA WEB"})

class SamplePageView(TemplateView):
	template_name = "core/sample.html"





class MainPageView(TemplateView):
	template_name = "core/base.html"

	


class PubListView(ListView):
    model = Publication
    template_name = 'core/home.html'
    paginate_by = 3
    

def my_view(request):
    """The view for your blog page"""
    publication_list = Publication.objects.all()
    profile_list = Profile.objects.all()

    template = loader.render_to_string('core/edit_main.html')
    context = RequestContext(request,{
        'publication_list': publication_list,
        'profile_list': profile_list,
    })
    return HttpResponse(template.render(context))