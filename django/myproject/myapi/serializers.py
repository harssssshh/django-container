from rest_framework import serializers
from .models import Hero
from .models import Containers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
 class Meta:
  model = Hero
  fields = ('name', 'alias')

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Containers
		fields = ('name', 'containerid')