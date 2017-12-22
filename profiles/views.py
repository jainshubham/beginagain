# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from django.views.generic import ListView, View
from profiles.models import Profile
from django.http import HttpResponse
from django.urls import reverse


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'profiles-listing.html'

    def get_queryset(self):
        gender = not self.request.__dict__['user'].gender
        queryset = Profile.objects.filter(gender=gender)
        return queryset


class ProfileView(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile-detail.html'

    def get_queryset(self):
        return get_object_or_404(Profile, id=self.kwargs['id'])


class ProfileMy(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile-my.html'

    def get_queryset(self):
        print('get')
        id = self.request.__dict__['user'].id
        return get_object_or_404(Profile, id=id)

    def post(self, request, *args, **kwargs):
        """Not sure why post is redirecting here

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # id = self.request.__dict__['user'].id
        # instance = Profile.objects.get(id=id)
        return HttpResponseRedirect('')

class LoginView(ListView):
    model = Profile
    context_object_name = 'profiles'


    def post(self, request, *args, **kwargs):
        """Not sure why post is redirecting here

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # id = self.request.__dict__['user'].id
        # instance = Profile.objects.get(id=id)
        print('here')
        return render(request, 'profiles-listing.html')
