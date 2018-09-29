from django.db import models

# Create your models here.

class Inmate(models.Model):
    person_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True)
    sex = models.CharField(max_length=6, choices=(
        ("male", "Male"),
        ("female", "Female")
    ))
    ethnicity = models.CharField(max_length=16, choices=(
        ('african-american', 'African American'),
        ('asian', 'Asian'),
        ('caucasian', 'Caucasian'),
        ('hispanic', 'Hispanic'),
        ('native-american', 'Native American'),
        ('other', 'Other')
    ))
    dob = models.DateField()
    
    legal_status = models.CharField(max_length=50)
    custody_status = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    language = models.CharField(max_length=7, choices=(
        ('english', 'English'),
        ('spanish', 'Spanish')
    ))


class Assessment(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE, related_name="assessments")
    date = models.DateField()
    case_id = models.IntegerField()
    assessment_id = models.IntegerField(unique=True)
    agency_text = models.CharField(max_length=255)
    supervision_level = models.IntegerField()

    violence_score_raw = models.FloatField(null=True)
    violence_score = models.IntegerField(null=True)

    recidivism_score_raw = models.FloatField(null=True)
    recidivism_score = models.IntegerField(null=True)

    fail_to_appear_score_raw = models.FloatField(null=True)
    fail_to_appear_score = models.IntegerField(null=True)

    type = models.CharField(max_length=4, choices=(('new', 'New'), ('copy', 'Copy')))
    reason = models.CharField(max_length=50)

    @property
    def violence_score_text(self):
        if self.violence_score:
            if self.violence_score <= 4:
                return "low"
            elif self.violence_score <= 7:
                return "medium"
            elif self.violence_score <= 10:
                return "high"

    @property
    def recidivism_score_text(self):
        if self.recidivism_score:
            if self.recidivism_score <= 4:
                return "low"
            elif self.recidivism_score <= 7:
                return "medium"
            elif self.recidivism_score <= 10:
                return "high"

    @property
    def fail_to_appear_score_text(self):
        if self.fail_to_appear_score:
            if self.fail_to_appear_score <= 4:
                return "low"
            elif self.fail_to_appear_score <= 7:
                return "medium"
            elif self.fail_to_appear_score <= 10:
                return "high"

    @property
    def supervision_level_text(self):
        if self.supervision_level == 1:
            return "low"
        elif self.supervision_level == 2:
            return "medium"
        elif self.supervision_level == 3:
            return "medium with override consideration"
        elif self.supervision_level == 4:
            return "high"
        raise ValueError("Unknown Value: {}".format(self.supervision_level))





    