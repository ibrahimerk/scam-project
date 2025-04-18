from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('date_reported', 'user', 'is_verified')

    def validate(self, data):
        required_fields = ['title', 'description', 'scam_type', 'location']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise serializers.ValidationError({
                'error': f'The following fields are required: {", ".join(missing_fields)}'
            })
        
        return data 