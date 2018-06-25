"""nier URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from account.views import UserListView
from assets.views import GetEcsInfoView, EcsListView, EcsWaitListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^assets/', include('assets.urls')),


    url(r'^$', TemplateView.as_view(template_name='login.html')),
    url(r'^login$', TemplateView.as_view(template_name='login_new.html')),
    url(r'^index.html$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^userlist.html$', UserListView.as_view(), name="userlist"),
    url(r'^userinfo.html$', TemplateView.as_view(template_name='userinfo.html')),
    url(r'^ecs.html$', GetEcsInfoView.as_view(), name='ecsinfo'),
    url(r'^ecslist.html$', EcsListView.as_view(),name='ecslist'),
    url(r'^ecswaitlist.html$', EcsWaitListView.as_view(),name='ecswaitlist')
]


