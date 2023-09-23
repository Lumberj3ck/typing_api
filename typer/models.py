from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=200)
    training_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.CASCADE, related_name='levels')
    language = models.ForeignKey('KeyBoardLayout', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.created_at}'

class KeyBoardLayout(models.Model):
    language = models.CharField(max_length=200, choices=[('EN', 'English'), ('RU', "Russian")])

    def __str__(self) -> str:
        return f'{self.language}'

class Difficulty(models.Model):
    difficulty = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.difficulty}'