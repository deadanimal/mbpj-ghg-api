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
    TicketAnswer,
    TicketQuestion
)

from .serializers import (
    TicketAnswerSerializer,
    TicketQuestionSerializer
)

class TicketAnswerViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketAnswer.objects.all()
    serializer_class = TicketAnswerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['submitted_by', 'date_submitted']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = TicketAnswer.objects.all()
        return queryset

class TicketQuestionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketQuestion.objects.all()
    serializer_class = TicketQuestionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['submitted_by', 'date_submitted']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = TicketQuestion.objects.all()
        return queryset