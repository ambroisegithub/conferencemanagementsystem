from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference
from .forms import ConferenceForm

def conference_list(request):
    conferences = Conference.objects.all()
    return render(request, 'conference_list.html', {'conferences': conferences})

def conference_detail(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'conference_detail.html', {'conference': conference})

def conference_create(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            conference = form.save()
            return redirect('conference_detail', pk=conference.pk)
    else:
        form = ConferenceForm()
    return render(request, 'conference_create.html', {'form': form})

def conference_edit(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        form = ConferenceForm(request.POST, instance=conference)
        if form.is_valid():
            conference = form.save()
            return redirect('conference_detail', pk=conference.pk)
    else:
        form = ConferenceForm(instance=conference)
    return render(request, 'conference_edit.html', {'form': form})

def conference_delete(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        conference.delete()
        return redirect('conference_list')
    return render(request, 'conference_delete.html', {'conference': conference})

def conference_schedule(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    return render(request, 'conference_schedule.html', {'conference': conference})
