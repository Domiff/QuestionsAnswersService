from rest_framework.serializers import ModelSerializer

from questions_answers_app.models import Answer


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = ["id", "question_id", "user_id", "text", "created_at"]
