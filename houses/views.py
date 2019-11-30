from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin


from django_filters.rest_framework import DjangoFilterBackend


from .models import (
    House, 
    HouseType
)

from .serializers import (
    HouseSerializer, 
    HouseTypeSerializer
)


class HouseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = House.objects.all()
        return queryset    



class HouseTypeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = HouseType.objects.all()
        return queryset        