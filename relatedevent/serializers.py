from django.db import models
from django.db.models import fields
from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers
from hashid_field.rest import HashidSerializerCharField

from relatedevent.models import ReportedEvent

class ReportedEventSerializer(serializers.HyperlinkedModelSerializer):
    coordenada = PointField()
    reported_hash = HashidSerializerCharField(source_field='relatedevent.ReportedEvent.reported_hash', read_only=True)
    
    class Meta:
        model = ReportedEvent
        fields = (
            'url',
            'coordenada', #{'latitude': 6.0794697, 'longitude': -49.8840777}
            'created',            
            'user_agent',
            'reported_hash',            
        )
        read_only_fields = [
            'user_agent',
        ]
        