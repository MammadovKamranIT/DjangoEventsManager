from django.contrib import messages
from django.middleware.csrf import get_token
from django.utils.html import escape

from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from events import data

from events.forms import ContactForm, EventForm
from events.models import Event

def index(request: HttpRequest):

    return render(request, 'events/home.html')


def about(request: HttpRequest):

    return render(request, 'events/about.html')



def contact(request: HttpRequest):
    form = ContactForm()
    return render(request, 'events/contact.html', {'form': form})



def events_view_list(request: HttpRequest) -> HttpResponse:

    
   
    events = Event.objects.filter(author=request.user)


    return render(request, 'events/events_list.html', {'events': events})


@login_required
def events_detail (request: HttpRequest, event_id: int) -> HttpResponse:


    event = get_object_or_404(Event.objects.select_related('author', "category").prefetch_related('tags'), pk=event_id)
   
    if event.author != request.user:

        return HttpResponseForbidden("You can only see notes owned by yourself")
    
    return render(request, 'events/event_detail.html', {'event': event})



@login_required
def events_create (
        request: HttpRequest
) -> HttpResponse:
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            form.save_m2m()
            messages.success(request, "Event created")            
            return redirect('events:events_detail', event_id=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_create.html', {'form': form})




def events_update(
        request: HttpRequest,
        event_id: int
) -> HttpResponse:
    event = data.get_event(event_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            current_status = form.cleaned_data['current_status'].split()
            data.update_event(
                event_id,
                title=title,
                content=content,
                category=category,
                current_status=current_status
            )
            return redirect('events_list')
    else:
        form = EventForm(initial=event)
    return render(request, 'events/event_create.html', {'form': form})

            

    


def events_delete (

    request: HttpRequest,
    event_id: int
) -> HttpResponse:
     
    event = get_object_or_404(Event, pk=event_id)
    if event.author != request.user:
    
        return HttpResponseForbidden("You can only delete events owned by yourself")

    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted")
        return redirect('events:events_list')
    return render(request, 'events/event_delete.html', {'event': event})


# events_delete()