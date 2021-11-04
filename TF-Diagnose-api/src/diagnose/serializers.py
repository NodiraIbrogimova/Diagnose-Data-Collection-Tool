from rest_framework import serializers

from src.diagnose.models import Diagnose


class DiagnoseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnose
        exclude = ("created_at", )
        read_only_fields = ("user",)