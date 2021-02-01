from rest_framework import serializers

from apps.accounts.models import Institution, Account


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        read_only_fields = (
            "id",
            "created_at",
            "access_token",
        )
        fields = (
            "id",
            "created_at",
            "access_token",
        )


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        read_only_fields = (
            "item_id",
            "created_at",
            "institution",
        )
        fields = (
            "item_id",
            "created_at",
            "institution",
        )
