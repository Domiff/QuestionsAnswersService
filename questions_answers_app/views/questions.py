from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)

from questions_answers_app.models import Question
from questions_answers_app.serializers import QuestionSerializer
from questions_answers_app.serializers import (
    QuestionSerializerWithAnswer,
)


class GetAllQuestion(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CreateQuestion(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class GetOneQuestion(RetrieveAPIView):
    queryset = Question.objects.prefetch_related("answers").all()
    serializer_class = QuestionSerializerWithAnswer
    lookup_field = "id"


class DeleteQuestion(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = "id"
