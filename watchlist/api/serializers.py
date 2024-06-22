from rest_framework import serializers
from rest_framework.decorators import api_view

@api_view
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    desc = serializers.CharField()
    active = serializers.BooleanField()