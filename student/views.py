from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def create(self, request, *args, **kwargs):
        age = int(request.data.get("age", 0))
        if age < 5:
            return Response({"error": "The age must be at least 5 years."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        student = self.get_object()
        if not student.is_active:
            return Response({"error": "You cannot edit an inactive student."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        student.is_active = False
        student.save()
        return Response({"message": "The student has been deactivated."}, status=status.HTTP_204_NO_CONTENT)
