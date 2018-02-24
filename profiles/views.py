# Create your views here.
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, RedirectView

from profiles.models import Profile


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'profiles-listing.html'

    # def get_queryset(self):
    #     gender = not self.request.user.gender
    #     # queryset = Profile.objects.filter(gender=gender)
    #     queryset = Profile.objects.all()
    #     return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        gender = not self.request.user.gender
        # Add in a QuerySet of all the books
        # context['profile'] = get_object_or_404(Profile, id=self.request.user.id)
        # context['choices'] = Profile.get_choices()
        # if they have received interest from us.
        context['selected_profiles'] = Profile.objects.filter(interest_received__id=self.request.user.id)
        context['new_profiles'] = Profile.objects.exclude(interest_received__id=self.request.user.id)
        return context


class ProfileView(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile-detail.html'
    #
    # def get_queryset(self):
    #     return get_object_or_404(Profile, id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['profile'] = get_object_or_404(Profile, id=self.request.user.id)
        # context['choices'] = Profile.get_choices()
        # if they have received interest from us.
        context['profile'] = Profile.objects.filter(id=self.kwargs['id'])
        context['my_profile'] = Profile.objects.filter(id=self.request.user.id)
        return context


class MyProfile(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile-my.html'
    #
    # def get_queryset(self):
    #     id = self.request.__dict__['user'].id
    #     return get_object_or_404(Profile, id=id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profile'] = get_object_or_404(Profile, id=self.request.user.id)
        context['choices'] = Profile.get_choices()
        # if they have received interest from us.
        context['selected_profiles'] = Profile.objects.filter(interest_received__id=self.request.user.id)
        context['new_profiles'] = Profile.objects.exclude(interest_received__id=self.request.user.id)
        return context

    def post(self, request, *args, **kwargs):
        """Not sure why post is redirecting here

        :param request:
        :param args:Profile
        :param kwargs:
        :return:
        """
        id = self.request.__dict__['user'].id
        instance = Profile.objects.get(id=id)
        for key in Profile._meta.get_fields():
            value = request.POST.get(key.name)
            if key.name == 'images':
                if value:
                    #print("images: {}".format(value))
                    value = key.upload_to + '/' + value
                    setattr(instance, key.name, value)
            elif key.name in ['height', 'weight']:
                setattr(instance, key.name, value.strip(' g').strip(' m'))
            elif value is not None:
                try:
                    print("{}, {}, {}, {}".format(key, type(key), value, type(value)))
                    setattr(instance, key.name, value)
                except:
                    print(key.name)
        instance.save()
        return HttpResponseRedirect('.')


class LoginView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'login.html'

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
        user = authenticate(request, email=email, password=password)
        if not user:
            raise Exception("provide valid email and password.")
        login(request, user)
        return HttpResponseRedirect('profiles/me/')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('profiles/me/')
        else:
            return render(request, self.template_name)


class LogoutView(RedirectView):
    next_page = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        # return super(LogoutView, self).get_redirect_url(request, *args, **kwargs)
        return HttpResponseRedirect('/')


class ShowInterest(ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile-my.html'

    def get_queryset(self):
        id = self.request.__dict__['user'].id
        instance = Profile.objects.get(id=id)
        target_instance = Profile.objects.get(id=self.kwargs['id'])
        instance.interest_shown.add(target_instance)
        return get_object_or_404(Profile, id=id)
