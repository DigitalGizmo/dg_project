"""gizmo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from sitewide.views import ProjectDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^projects/$', TemplateView.as_view(template_name="projects.html"), name='projects'),
    url(r'^services/$', TemplateView.as_view(template_name="services.html"), name='services'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    # url(r'^$', views.HomeTemplateView.as_view(), name='home'),
    url(r'^projects/ajax/(?P<slug>\S+)/$', ProjectDetailView.as_view(), name='project_detail'),
    url(r'^projects/(?P<slug>\S+)/$', 
        ProjectDetailView.as_view(template_name="projects/project_full.html"), 
        name='project_full'),
    url(r'^about/ajax/(?P<slug>\S+)/$', ProjectDetailView.as_view(), name='about_detail'),
    url(r'^about/(?P<slug>\S+)/$', 
        ProjectDetailView.as_view(template_name="projects/project_full.html"), 
        name='about_full'),

]
