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

from .models import (
    Report
)

from .serializers import (
    ReportSerializer
)

def create_pdf(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    #html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response

class ReportViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    #filterset_fields = ['application_id']

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
        #paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
        html_string = render_to_string('pdf_template.html')

        html = HTML(string=html_string)
        pdf_file = html.write_pdf()

        #fs = FileSystemStorage('/tmp')
        #with fs.open('GHG_Report.pdf') as pdf:
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="GHG_Report.pdf"'
        #response['Content-Disposition'] = 'attachment;filename="GHG_Report.pdf"'
        #return response

        return response
        #create_pdf(request)
        #return super().create(request)