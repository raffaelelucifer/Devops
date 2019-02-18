"""Devops URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from scanhosts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_number/$', views.getnumber_of_assets),
    url(r'^getphyinfo_list/$', views.getinfo_from_physical),
    url(r'^getvirinfo_list/$', views.getinfo_from_virtual),
    url(r'^add_productinfo/$', views.add_productinfo),
    url(r'^get_productinfo/$', views.getinfo_from_product),
    url(r'^add_projectinfo/$', views.add_projectinfo),
    url(r'^get_projectinfo/$', views.getinfo_from_project),
]
