from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .filters import ProfilesFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 8





class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
"""
@login_required
def profile_list(request):
    f = ProfilesFilter(request.GET, queryset=Profile.objects.all())
    return render(request, 'profiles/filter.html', {'filter':f})
    
    """


def profile_list(request):
    f = ProfilesFilter(request.GET, queryset=Profile.objects.all())

    paginator = Paginator(f.qs, 8)
    page = request.GET.get('page')

    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(request, 'profiles/filter.html', {'filter':response, 'fil':f})


