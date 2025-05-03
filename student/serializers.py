from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_age(self, value):
        if value < 5:
            raise serializers.ValidationError("The age must be at least 5 years.")
        return value
