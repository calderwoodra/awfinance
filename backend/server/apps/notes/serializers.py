from apps.notes.models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = (
            "id",
            "created_at",
            "created_by",
        )
        fields = (
            "id",
            "created_at",
            "created_by",
            "content"
        )
