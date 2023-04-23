from rest_framework import serializers
from .models import Tags, Notes


class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    notes = NotesSerializer(many=True, read_only=True)

    class Meta:
        model = Tags
        fields = '__all__'


class CombinedSerializer(serializers.Serializer):
    notes = NotesSerializer(many=True)
    tags = TagsSerializer(many=True)
