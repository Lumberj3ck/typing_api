import re
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from typer.serializers import LevelSerializer, DifficultySerializer
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from .models import Level, Difficulty


class LevelsApiView(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def list(self, request):
        lang = request.GET.get('language', '')
        lang_number = re.search('\d+', lang)
        filters = {'language': int(lang_number.group())} if lang else {}
        queryset = Level.objects.filter(**filters)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def next_level(self, request, level_id, *args, **kwargs):
        next = Level.objects.filter(id__gt=level_id).order_by('id').first()
        if next:
            serializer = self.get_serializer(next)
            return Response(serializer.data)
        return Response({'next': 'null'})
        


class DifficultyApiView(ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
