# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.views.generic import ListView
from profiles.models import Profile


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


class MyProfile(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile-my.html'

    def get_queryset(self):
        id = self.request.__dict__['user'].id
        return get_object_or_404(Profile, id=id)

    def post(self, request, *args, **kwargs):
        """Not sure why post is redirecting here

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        id = self.request.__dict__['user'].id
        instance = Profile.objects.get(id=id)
        for key in Profile._meta.get_fields():
            setattr(instance, key.name, request.POST.get(key.name))
        instance.save()
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
        return HttpResponseRedirect('') #render(request, 'profiles-listing.html')
