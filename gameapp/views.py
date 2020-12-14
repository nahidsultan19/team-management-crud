from django.shortcuts import render

# Create your views here.
from .models import Team


def index(request):

    context = {
        'teams': Team.objects.filter(team_level__exact="U09")
    }
    return render(request, 'home.html', context)
