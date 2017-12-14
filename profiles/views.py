from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView
from profiles.models import Profile


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    queryset = Profile.objects.filter()
    template_name = 'profiles-listing.html'


class ProfileView(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile-detail.html'


    def get_queryset(self):
        return get_object_or_404(Profile, id=self.kwargs['pk'])

