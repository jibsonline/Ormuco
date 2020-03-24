from django.shortcuts import render, redirect, get_object_or_404
from .models import FavDetails
from .forms import FavsForm
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'favsapp/index.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return FavDetails.objects.all()


class ContactDetailView(DetailView):
    model = FavDetails
    template_name = 'favsapp/contact-detail.html'


def create(request):
    if request.method == 'POST':
        form = FavsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    #form = FavsForm()

    return render(request, 'favsapp/create.html', {'form': form})
