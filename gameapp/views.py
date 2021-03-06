from django.shortcuts import render, redirect

# Create your views here.
from .models import Team
from .forms import TeamForm


def form(request):
    # t_form = TeamForm()
    context = {
        'form': TeamForm(),
        'teams': Team.objects.all()

    }
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TeamForm()
    return render(request, 'form.html', context)


def Update(request, pk):
    team = Team.objects.get(id=pk)
    form = TeamForm(instance=team)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'update-form.html', context)


def Delete(request, pk):
    delete_item = Team.objects.get(id=pk)
    if request.method == 'POST':
        delete_item.delete()
        return redirect('home')
    context = {'delete': delete_item}
    return render(request, 'delete-item.html', context)
