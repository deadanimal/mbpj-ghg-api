from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from django.template.loader import render_to_string
from weasyprint import HTML
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from .models import (
    Report
)

from .serializers import (
    ReportSerializer
)


class ReportViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_fields = ['application_id']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Report.objects.all()
        return queryset

    def create(self, request):
        html_string = render_to_string('pdf_template.html')

        html = HTML(string=html_string)
        pdf_file = html.write_pdf()# you alreagdy generated a PDF file instance

        # TODO: save pdf file instance into django-storage
        # TODO: get the URL of the file instance that was saved in django-storage
        saved_url_path = default_storage.save(
            'GHG_Report.pdf', 
            ContentFile(pdf_file)
        )
        full_url_path = settings.MEDIA_ROOT + saved_url_path

        Report.objects.create(
            # name
            pdf_file_url=full_url_path
        )

        return super().create(request)
