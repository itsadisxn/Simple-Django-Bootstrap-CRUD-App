"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.urls import path
from django.http import HttpRequest
from .models import Profile
from django.views.generic import FormView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


class ProfileListView(ListView):
    model = Profile

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProfileListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Users'
        context['message'] = 'given below is a list of all users'
        return context

class ProfileCreateView(CreateView):
    model = Profile
    fields = ['user', 'display_name', 'profile_type', 'location', 'biography']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProfileCreateView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Create User'
        context['message'] = 'please use the form below to create the user'
        return context

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'User Detail'
        context['message'] = 'given below are the details of the user'
        return context

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['user', 'display_name', 'profile_type', 'location', 'biography']

    def get_success_url(self):
        return reverse('profile-detail', kwargs={'pk' : self.object.pk})
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Update User'
        context['message'] = 'please use the form below to update the user'
        return context

class ProfileDeleteView(DeleteView):
    model = Profile
    template = 'profile_confirm_delete.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProfileDeleteView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Delete User'
        context['message'] = 'please use the form below to delete the user'
        return context