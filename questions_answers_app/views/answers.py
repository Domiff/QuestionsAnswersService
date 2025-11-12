from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView

from questions_answers_app.models import Answer
from questions_answers_app.serializers import AnswerSerializer


class CreateAnswer(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class GetAnswer(RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = "id"


class DeleteAnswer(DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = "id"
