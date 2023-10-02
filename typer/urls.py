from django.urls import path
from typer.views import LevelsApiView, DifficultyApiView, LanguageApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('levels/difficulties', DifficultyApiView)
router.register('levels', LevelsApiView)


urlpatterns = [
    path('levels/next/', LevelsApiView.as_view({'get': 'next_level'})),
    path('levels/languages/', LanguageApiView.as_view()),
]
urlpatterns += router.urls