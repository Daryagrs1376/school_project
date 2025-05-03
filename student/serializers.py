from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    is_active_status = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    
    def get_is_active_status(self, obj):
        if obj.is_active:
            return "Active"
        else:
            return "Inactive"
        


    def validate_age(self, value):
        if value < 5:
            raise serializers.ValidationError("The age must be at least 5 years.")
        return value
