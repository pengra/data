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
    ethnicity = models.CharField(max_length=50)
    dob = models.DateField()
    
    legal_status = models.CharField(max_length=50)
    custody_status = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=50)
    language = models.CharField(max_length=50)




class Assessment(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE, related_name="assessments")
    date = models.DateField()
    case_id = models.IntegerField()
    assessment_id = models.IntegerField()
    agency_text = models.CharField(max_length=255)
    supervision_level = models.IntegerField()

    violence_score_raw = models.FloatField()
    violence_score = models.IntegerField()

    recidivism_score_raw = models.FloatField()
    recidivism_score = models.IntegerField()

    violence_score_raw = models.FloatField()
    violence_score = models.IntegerField()

    type = models.CharField(max_length=50)
    

    @property
    def supervision_level_text(self):
        if self.supervision_level == 1:
            return "Low"
        elif self.supervision_level == 2:
            return "Medium"
        elif self.supervision_level == 3:
            return "Medium with Override Consideration"
        elif self.supervision_level == 4:
            return "High"
        raise ValueError("Unknown Value: {}".format(self.supervision_level))





    