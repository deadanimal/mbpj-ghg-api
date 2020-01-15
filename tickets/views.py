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
    TicketQuestion,
    TicketEvent
)

from .serializers import (
    TicketAnswerSerializer,
    TicketQuestionSerializer,
    TicketEventSerializer
)

def testing_get(self):
    something = self.request.user
    #something_else = self.request.ticket_question
    print(something)

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
    
    def create(self, request):
        #print("testtest")
        #print(self.request.user.full_name)
        TicketEvent.objects.create(
            action = 'Create ticket answer',
            action_by = self.request.user
        )
        return super().create(request)
    

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
        testing_get(self)
        return queryset

    def create(self, request):
        #print("testtest")
        #print(self.request.user.full_name)
        TicketEvent.objects.create(
            action = 'Create ticket question',
            action_by = self.request.user
        )
        return super().create(request)

class TicketEventViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = TicketEvent.objects.all()
    serializer_class = TicketEventSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['action_by', 'date_time']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
    
    def get_queryset(self):
        queryset = TicketEvent.objects.all()
        #testing_get(self)
        return queryset
    
