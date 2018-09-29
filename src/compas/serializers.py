from rest_framework import serializers
from compas.models import Assessment


class AssessmentSerializers(serializers.ModelSerializer):
    supervision_level_text = serializers.CharField(read_only=True)
    inmate_id = serializers.IntegerField(source='inmate.person_id', read_only=True)
    inmate_sex = serializers.CharField(source='inmate.sex', read_only=True)
    inmate_ethnicity = serializers.CharField(source='inmate.ethnicity', read_only=True)
    inmate_dob = serializers.CharField(source='inmate.dob', read_only=True)
    inmate_legal_status = serializers.CharField(source='inmate.legal_status', read_only=True)
    inmate_custody_status = serializers.CharField(source='inmate.custody_status', read_only=True)
    inmate_marital_status = serializers.CharField(source='inmate.marital_status', read_only=True)
    inmate_language = serializers.CharField(source='inmate.language', read_only=True)

    class Meta:
        model = Assessment
        lookup_field = 'assessment_id'
        fields = [
            'inmate_id',
            'inmate_sex',
            'inmate_ethnicity',
            'inmate_dob',
            'inmate_legal_status',
            'inmate_custody_status',
            'inmate_marital_status',
            'inmate_language',
            'date',
            'case_id',
            'assessment_id',
            'agency_text',
            'supervision_level',
            'supervision_level_text',
            'violence_score',
            'violence_score_text',
            'recidivism_score',
            'recidivism_score_text',
            'fail_to_appear_score',
            'fail_to_appear_score_text',
            'type',
        ]