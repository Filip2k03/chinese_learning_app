# chinese_learning/models.py
from django.db import models

class Vocabulary(models.Model):
    word_simplified = models.CharField(max_length=255, unique=True)
    pinyin = models.CharField(max_length=255, blank=True, null=True)
    definition_en = models.TextField(blank=True, null=True)
    example_sentence_zh = models.TextField(blank=True, null=True)
    example_sentence_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.word_simplified