# Create your views here.
from django.contrib.auth import authenticate

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
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
            value = request.POST.get(key.name)
            if value:
                setattr(instance, key.name, value)
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
        email = request.POST.get('email')
        password = request.POST.get('psw')
        if not (email and password):
            raise Exception("provide valid email and password.")
        user = authenticate(email=email, password=password)
        if not user:
            raise Exception("provide valid email and password.")
        profile = Profile.objects.get(email=email)
        return render(request, 'profiles-listing.html',  {
            'profiles': [profile]
        },)


class ShowInterest(ListView):
    model = Profile
    context_object_name = 'profile'

    def get_queryset(self):
        id = self.request.__dict__['user'].id
        instance = Profile.objects.get(id=id)
        target_instance = Profile.objects.get(id=self.kwargs['id'])
        instance.interest_shown.add(target_instance)
        return get_object_or_404(Profile, id=id)