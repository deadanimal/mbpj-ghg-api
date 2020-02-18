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
    HouseEvent
)

from .serializers import (
    HouseSerializer,
    HouseEventSerializer
)

class HouseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['building_type', 'applicant', 'assessment_tax_account', 'postcode', 'area']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = House.objects.all()
        return queryset
    
    def create(self, request):
        HouseEvent.objects.create(
            action = 'Create house',
            action_by = self.request.user
        )
        return super().create(request)
    
    def update(self, request, pk=None):
        HouseEvent.objects.create(
            action = 'Update house details',
            action_by = self.request.user
        )
        return super().update(request)

class HouseEventViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = HouseEvent.objects.all()
    serializer_class = HouseEventSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['action_by', 'date_time']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
    
    def get_queryset(self):
        queryset = HouseEvent.objects.all()
        return queryset