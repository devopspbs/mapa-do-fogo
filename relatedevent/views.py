from django.db.models import query
from django.shortcuts import render
from relatedevent import serializers
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle  

from relatedevent.models import ReportedEvent
                    
from relatedevent.serializers import ReportedEventSerializer

# Create your views here.

"""
Views de teste para o model Bairro.
"""
class ReportedEventList(generics.ListCreateAPIView):
    # throttle_scope = 'reportedevents' 
    # throttle_classes = (ScopedRateThrottle,)     
    queryset = ReportedEvent.objects.all()
    serializer_class = ReportedEventSerializer
    name = 'reportedevent-list'
    
    def perform_create(self, serializer):
        serializer.save(
            user_agent=self.request.headers['User-Agent'] + " " + self.request.headers['Host'] + " " + self.request.headers['Origin'], 
            #reported_hash=hash(self.request.headers['User-Agent'])
        )

class ReportedEventDetail(generics.RetrieveAPIView):
    queryset = ReportedEvent.objects.all()
    serializer_class = ReportedEventSerializer
    name = 'reportedevent-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'reportedevents': reverse(ReportedEventList.name, request=request),
        })