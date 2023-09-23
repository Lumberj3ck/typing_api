from django.contrib import admin
from .models import * 

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    pass

@admin.register(KeyBoardLayout)
class KeyboardsAdmin(admin.ModelAdmin):
    pass
