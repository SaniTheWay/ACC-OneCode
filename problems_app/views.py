from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from problems_app.models import Problem
from problems_app.serializers import ProblemSerializer
# Create your views here.

class ProblemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.IsAuthenticated]