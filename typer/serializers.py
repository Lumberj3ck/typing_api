from rest_framework import serializers
from .models import Level, Difficulty


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'training_text', 'created_at', 'difficulty', 'name', 'language')


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty 
        fields = '__all__'
