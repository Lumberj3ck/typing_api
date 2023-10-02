import re
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from typer.serializers import LevelSerializer, DifficultySerializer, Keyboard_layout_Serializer
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from .models import Level, Difficulty, KeyBoardLayout


class LevelsApiView(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def list(self, request):
        lang = request.GET.get('language', '')
        filters = {'language': self.get_digits_from_params(lang)} if lang else {}
        queryset = Level.objects.filter(**filters)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_digits_from_params(self, param):
        number = re.search('\d+', param)
        return int(number.group()) if number else None

    def next_level(self, request, *args, **kwargs):
        lang_code = request.GET.get('lang_code', '')
        level_id = request.GET.get('level_id', '')
        next = Level.objects.filter(id__gt=self.get_digits_from_params(level_id), language=self.get_digits_from_params(lang_code)).order_by('id').first()
        if next:
            serializer = self.get_serializer(next)
            return Response(serializer.data)
        return Response({'next': 'null'})
        

class LanguageApiView(APIView):
    def get(self, request):
        serializer = Keyboard_layout_Serializer(KeyBoardLayout.objects.all(), many=True)
        return Response(serializer.data) 

class DifficultyApiView(ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
