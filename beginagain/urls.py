"""beginagain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

# from django.urls import reverse_lazy

from profiles.views import (
    MyProfile,
    LoginView,
    LogoutView,
    ProfileListView,
    ProfileView,
    ShowInterest
)

urlpatterns = [
    url(r'^$', LoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^profiles/me/$', MyProfile.as_view()),
    url(r'^profiles/(?P<id>\d+)/$', ProfileView.as_view()),
    url(r'^profiles/$', ProfileListView.as_view()),
    url(r'^profiles/(?P<id>\d+)/show-interest$', ShowInterest.as_view()),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    # url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login'))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


