from django.conf import settings
from django.db import models

from src.diagnose import (
    Gender,
    Symptom,
    TestType,
    SpecimenType
)



class Diagnose(models.Model):
    sao2_std = models.IntegerField(null=True, blank=True)
    heart_rate_mean = models.IntegerField(null=True, blank=True)
    respiratory_rate_mean = models.IntegerField(null=True, blank=True)
    respiratory_rate_std = models.IntegerField(null=True, blank=True)
    heart_rate_alarm_low_max = models.IntegerField(null=True, blank=True)
    sao2_mean = models.IntegerField(null=True, blank=True)

    temperature_mean = models.IntegerField(null=True, blank=True)
    temperature_std = models.IntegerField()
    skin_temperature_std = models.IntegerField()
    skin_temperature_mean = models.IntegerField(null=True, blank=True)

    blood_pressure_std = models.IntegerField(null=True, blank=True)
    blood_pressure_mean = models.IntegerField(null=True, blank=True)
    blood_pressure_systolic_std = models.IntegerField(null=True, blank=True)
    blood_pressure_systolic_mean = models.IntegerField(null=True, blank=True)
    blood_pressure_diastolic_std = models.IntegerField(null=True, blank=True)
    blood_pressure_diastolic_mean = models.IntegerField(null=True, blank=True)

    d10w_amount = models.IntegerField()
    prescription_count = models.IntegerField()
    date_event_count = models.IntegerField()
    white_blood_count = models.IntegerField()
    platelet = models.IntegerField()

    is_recently_traveled = models.BooleanField()
    gender = models.CharField(max_length=20, choices=Gender.choices)
    symptom = models.CharField(max_length=30, choices=Symptom.choices)
    laboratory_type = models.CharField(max_length=30, choices=TestType.choices)
    collected_specimen_type = models.CharField(max_length=20, choices=SpecimenType.choices)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="diagnoses"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"
