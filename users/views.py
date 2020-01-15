from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['user_type'] = user.user_type

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

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
    CustomUser,
    UserOccupation,
    UserEvent
)

from .serializers import (
    CustomUserSerializer,
    UserOccupationSerializer,
    UserEventSerializer
)

class CustomUserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['user_type', 'gender', 'occupation']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        return queryset
    
    def update(self, request, pk=None):
        UserEvent.objects.create(
            action = 'Update user details',
            action_by = self.request.user
        )
        return super().update(request)

class UserOccupationViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = UserOccupation.objects.all()
    serializer_class = UserOccupationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = UserOccupation.objects.all()
        return queryset

class UserEventViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = UserEvent.objects.all()
    serializer_class = UserEventSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['action_by', 'date_time']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]    
    
    def get_queryset(self):
        queryset = UserEvent.objects.all()
        testing_get(self)
        return queryset
        