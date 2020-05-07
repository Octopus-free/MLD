from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import AlgorithmsBook, MetricsBook


class AlgorithmsBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlgorithmsBook
        fields = '__all__'


class MetricsBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetricsBook
        fields = '__all__'



