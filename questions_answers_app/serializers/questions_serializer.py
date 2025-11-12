from rest_framework.serializers import ModelSerializer

from questions_answers_app.models import Question
from .answers_serializer import AnswerSerializer


class QuestionSerializer(ModelSerializer):

    class Meta:
        model = Question
        fields = ["id", "text", "created_at"]


class QuestionSerializerWithAnswer(ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "created_at", "answers"]
