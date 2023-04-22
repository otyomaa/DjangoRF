from rest_framework import serializers
from .models import Tags, Notes


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    Tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Notes
        fields = '__all__'
