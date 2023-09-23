from django.urls import path
from typer.views import LevelsApiView, DifficultyApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('levels/difficulties', DifficultyApiView)
router.register('levels', LevelsApiView)

print(router.urls)
urlpatterns = [
    path('levels/next/<int:level_id>/', LevelsApiView.as_view({'get': 'next_level'}))
]
urlpatterns += router.urls