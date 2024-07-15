from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Event, Participation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def home(request):
    """
    Render the home page.

    Parameters:
    request (HttpRequest): The request object used to generate the response.

    Returns:
    HttpResponse: The rendered home page.
    """
    return render(request, 'campaign/home.html')

def about(request):
    """
    Render the about page.

    Parameters:
    request (HttpRequest): The request object used to generate the response.

    Returns:
    HttpResponse: The rendered about page.
    """
    return render(request, 'campaign/about.html')

def events(request):
    """
    Render the events page with a list of all events.

    Parameters:
    request (HttpRequest): The request object used to generate the response.

    Returns:
    HttpResponse: The rendered events page with a list of events.
    """
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'campaign/events.html',context)

def join_event(request):
    """
    Handle the joining of an event by a user.

    If the request method is POST, the function checks if the user is authenticated,
    retrieves the event by name, and creates a Participation record for the user.

    Parameters:
    request (HttpRequest): The request object used to generate the response.

    Returns:
    HttpResponse: A redirect to the events page if the method is POST, otherwise a 405 status code.
    """
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event = get_object_or_404(Event, name=event_name)
        participation, created = Participation.objects.get_or_create(event=event, user=request.user)

        if created:
            messages.success(request, f'Thank you for joining the {event_name}!')
        else:
            messages.info(request, f'You have already joined the {event_name}.')

        return redirect('events_page') 
    return HttpResponse(status=405)  

def events_page(request):
    """
    Render the events page with a list of all events.

    Parameters:
    request (HttpRequest): The request object used to generate the response.

    Returns:
    HttpResponse: The rendered events page with a list of events.
    """
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'campaign/events.html', context)

def join_event(request):
    """
    Handle the joining of an event by a user.

    If the request method is POST, the function checks if the user is authenticated,
    retrieves the event by name, and creates a Participation record for the user.

    Parameters:
    request (HttpRequest): The request object used to generate the response.

    Returns:
    HttpResponse: A redirect to the events page if the method is POST, otherwise a 405 status code.
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to join an event.')
            return redirect('register')

        event_name = request.POST.get('event_name')
        event = get_object_or_404(Event, name=event_name)
        participation, created = Participation.objects.get_or_create(event=event, user=request.user)

        if created:
            messages.success(request, f'Thank you for joining the {event_name}!')
        else:
            messages.info(request, f'You have already joined the {event_name}.')

        return redirect('events_page') 
    return HttpResponse(status=405)  

def register(request):
    """
    Handle user registration.

    If the request method is POST, the function processes the registration form.
    If the form is valid, it saves the new user and redirects to the login page.

    Parameters:
    request (HttpRequest): The request object used to generate the response.

    Returns:
    HttpResponse: The rendered registration page with the registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


