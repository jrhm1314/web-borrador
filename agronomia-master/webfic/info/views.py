from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Publication
from registration.forms import PublicationForm, EstatusForm
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .filters import PublicationFilter
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
@method_decorator(login_required, name='dispatch')
class InfoListView(ListView):
    model = Publication
    template_name = 'info/info_list.html'
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class FiltroListView(ListView):
    model = Publication
    template_name = 'info/filtro_list.html'
    paginate_by = 5

"""@method_decorator(login_required, name='dispatch')"""
class InfoDetailView(FormMixin, DetailView):
    model = Publication
    form_class = EstatusForm
    success_url = reverse_lazy('home')
    template_name = 'info/info_detail.html'





"""
    def get_object(self):
        return get_object_or_404(Publication, user__username=self.kwargs['username'])
"""
"""
@login_required
def publication_list(request):
    f = PublicationFilter(request.GET, queryset=Publication.objects.all())
   
    return render(request, 'info/filter.html', {'filter':f})
"""



"""@login_required"""
def publication_list(request):
    f = PublicationFilter(request.GET, queryset=Publication.objects.all())

    paginator = Paginator(f.qs, 5)
    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'info/filter.html', {'filter':response, 'fil':f})


