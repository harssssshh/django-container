import docker

from django.shortcuts import render
from django.views.generic import TemplateView
from . import services
# Create your views here.

from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from .serializers import ContainerSerializer
from .models import Containers
from django.http import HttpResponseRedirect

# class HeroViewSet(viewsets.ModelViewSet):
#  queryset = Hero.objects.all().order_by('name')
#  serializer_class = HeroSerializer

class GetContainers(TemplateView):
 template_name = 'droplets.html'	
 # def start_container(request):
 #    if(request.GET.get('mybutton')):
 #     client = docker.APIClient(base_url='tcp://192.168.0.106:2375')
 #     container_name = client.rename(container="naughty_wilson", name="Alpine-Container")
 #     return request  
 # queryset = Containers.objects.all().order_by('name')
 # serializer_class = ContainerSerializer
 
 # def get_context_data(self, *args, **kwargs):
 #  context = {
 #            'containers' : services.mo-ify_stats()
 #        }     
 #  return context

def start_container(request):

    # return HttpResponseRedirect("login")
    #if(request.GET.get('mybutton')):
	client = docker.APIClient(base_url='tcp://192.168.0.106:2375')
	container_name = client.rename(container="Alpine", name="New-Alpine")
	return render(request, 'droplets.html')
    # else:
    # 	return HttpResponseRedirect("login")	