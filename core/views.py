from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import School, SchoolClass, Student
from .serializers import SchoolSerializer, SchoolClassSerializer, StudentSerializer

def home(request):
    """
    Display the homepage
    """
    return render(request, 'core/home.html')

class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows schools to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        """Delete all schools"""
        School.objects.all().delete()
        return Response({"message": "All schools have been deleted."}, status=status.HTTP_204_NO_CONTENT)

class SchoolClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows school classes to be viewed or edited.
    """
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
    
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        """Delete all school classes"""
        SchoolClass.objects.all().delete()
        return Response({"message": "All school classes have been deleted."}, status=status.HTTP_204_NO_CONTENT)

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        """Delete all students"""
        Student.objects.all().delete()
        return Response({"message": "All students have been deleted."}, status=status.HTTP_204_NO_CONTENT)
