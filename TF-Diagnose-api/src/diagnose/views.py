import pandas as pd
import io, csv
from datetime import datetime

from django.db.models import F
from django.http import HttpResponse
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from src.core.pagination import DiagnosePagination
from src.diagnose.models import Diagnose

from src.diagnose.serializers import (
    DiagnoseCreateSerializer
)


class DiagnoseViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializer_class = DiagnoseCreateSerializer
    queryset = Diagnose.objects.all()
    pagination_class = DiagnosePagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["GET"], detail=False, url_path='export-to-csv')
    def export_to_csv(self, request):
        qs = self.filter_queryset(self.get_queryset())
        df_output = pd.DataFrame(
            qs.annotate(
                first_name=F("user__first_name"),
                last_name=F("user__last_name"),
                email=F("user__email"),
                country=F("user__country"),
                place=F("user__place"),
                household_contact=F("user__household_contact")
            ).values(
                "sao2_std",
                "heart_rate_mean",
                "respiratory_rate_mean",
                "respiratory_rate_std",
                "heart_rate_alarm_low_max",
                "sao2_mean",
                "temperature_mean",
                "temperature_std",
                "skin_temperature_std",
                "skin_temperature_mean",
                "blood_pressure_std",
                "blood_pressure_mean",
                "blood_pressure_systolic_std",
                "blood_pressure_systolic_mean",
                "blood_pressure_diastolic_std",
                "blood_pressure_diastolic_mean",
                "d10w_amount",
                "prescription_count",
                "date_event_count",
                "white_blood_count",
                "platelet",
                "is_recently_traveled",
                "gender",
                "symptom",
                "laboratory_type",
                "collected_specimen_type",
                "first_name",
                "last_name",
                "email",
                "country",
                "place",
                "household_contact",
            )
        )
        df_output.columns = [
            "SaO2 (std)",
            "Heart Rate (mean)",
            "Respiratory Rate (mean)",
            "Respiratory Rate (std)",
            "Heart Rate Alarm Low (max)",
            "SaO2 (mean)",
            "Temperature (mean)",
            "Temperature (std)",
            "Skin Temperature (std)",
            "Skin Temperature_mean)",
            "Blood Pressure (std)",
            "Blood Pressure (mean)",
            "Blood Pressure Systolic (std)",
            "Blood Pressure Sytolic (mean)",
            "Blood Pressure Diastolic (std)",
            "Blood Pressure Diastolic (mean)",
            "D10W Amount",
            "Prescription Count",
            "Date Event Count",
            "White Blood Count",
            "Platelet",
            "Is Recently Traveled",
            "Gender",
            "Symptom",
            "Laboratory Test Undetaken",
            "Type of Specimen Collected",
            "First Name",
            "Last Name",
            "Email",
            "Country of Residence",
            "Place of Residence",
            "Household Contact",
        ]
        buffer = io.StringIO()
        csv.writer(buffer, quoting=csv.QUOTE_ALL)
        df_output.to_csv(buffer, index=False)
        buffer.seek(0)
        response = HttpResponse(buffer.read(),content_type="text/csv")
        response['Content-Disposition'] = f"attachment; filename=diagnose-{datetime.now().strftime('%d_%m_%Y')}.csv"
        return response
