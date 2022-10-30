from rest_framework import serializers
from problems_app.models import Problem, Prob_type

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'