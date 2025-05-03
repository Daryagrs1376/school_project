from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

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
