from rest_framework import serializers
from .models import Level, Difficulty, KeyBoardLayout


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'training_text', 'created_at', 'difficulty', 'name', 'language')


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty 
        fields = '__all__'

class Keyboard_layout_Serializer(serializers.ModelSerializer):
    class Meta:
        model = KeyBoardLayout 
        fields = '__all__'
