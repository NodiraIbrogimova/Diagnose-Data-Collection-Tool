class Gender:
    MALE = "male"
    FEMALE = "female"

    choices = (
        (MALE, MALE),
        (FEMALE, FEMALE)
    )


class Symptom:
    DIARRHEA = "diarrhea"
    COUGH = "cough"
    HIGH_FEVER = "high_fever"
    LOSS_OF_APPETITE = "loss_of_appetite"

    choices = (
        (DIARRHEA, DIARRHEA),
        (COUGH, COUGH),
        (HIGH_FEVER, HIGH_FEVER),
        (LOSS_OF_APPETITE, LOSS_OF_APPETITE),
    )


class TestType:
    BLOOD = "blood"
    STOOL = "stool"
    WIDAL = "widal"

    choices = (
        (BLOOD, BLOOD),
        (STOOL, STOOL),
        (WIDAL, WIDAL),
    )


class SpecimenType:
    BLOOD = "blood"
    URINE = "urine"

    choices = (
        (BLOOD, BLOOD),
        (URINE, URINE)
    )
