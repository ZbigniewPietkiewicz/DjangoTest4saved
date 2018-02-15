from rest_framework import serializers
from . import models

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'choice_text',
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


class PollLookupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'id',
                'poll_text',
                'pub_date'
        )
        model = models.Poll

# class ChoiceResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'choice_text',
#             'votes'
#         )
#         model = models.Choice


# class QuestionResultSerializer(serializers.ModelSerializer):
#     choices = ChoiceResultSerializer(many = True)
#     class Meta:
#         fields = (
#             'id',
#             'question_text',
#             'choices'
#         )
#         model = models.Question

# class PollResultSerializer(serializers.ModelSerializer):
#     questions = QuestionResultSerializer(many = True)
#     class Meta:
#         fields = (
#             'id',
#             'poll_text',
#             'questions'
#         )
#         model = models.Poll

class ChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id'
        )
        model = models.Choice
        
class QuestionAnswerSerializer(serializers.ModelSerializer):
    choice = ChoiceAnswerSerializer()
    class Meta:
        fields = (
            'id',
            'choice'
        )
        model = models.Question

class PollAnswerSerializer(serializers.ModelSerializer):
    questions = QuestionAnswerSerializer(many = True, read_only = True)
    class Meta:
        fields = (
            'id',
            'questions'
        )
        model = models.Poll
    def update(self,validated_data):
        questions_data = validated_data.pop('questions')
        for question in questions_data:
            choices = question.pop('choice')
            for choice in choices:
                selectedChoice = models.Choice.objects.get(id=choice['id'])
                selectedChoice.votes = selectedChoice.votes + 1
                selectedChoice.save()
        return True
            
        


            
            