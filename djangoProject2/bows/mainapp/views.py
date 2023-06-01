from django.shortcuts import render
from .models import Bow
from django.views.generic import DetailView


def index(request):
    bow = Bow.objects.all()
    print(bow)
    return render(request, 'main/index.html', {'bow': bow})

class BowDetailView(DetailView):
    model = Bow
    template_name = 'main/details_view.html'
    context_object_name = 'bow'




def about(request):

    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
