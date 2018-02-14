from rest_framework import serializers
from . import models

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'choice_text',
            'votes'
        )
        model = models.Choice

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        fields = (
                'id',
                'question_text',
                'choices'
        )
        model = models.Question

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many = True)
    class Meta:
        fields = (
                'id',
                'poll_text',
                'pub_date',
                'questions'
        )
        model = models.Poll

