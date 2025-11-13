import pytest

from questions_answers_app.serializers import (
    QuestionSerializer,
    AnswerSerializer,
    QuestionSerializerWithAnswer,
)


@pytest.mark.django_db
def test_question_serializer(question_factory):
    question = question_factory()
    serializer = QuestionSerializer(question)
    data = serializer.data
    assert data["id"] == question.id
    assert isinstance(data["text"], str)


@pytest.mark.django_db
def test_question_with_answer_serializer(question_factory, answer_factory):
    question = question_factory(text="Как дела?")

    answer1 = answer_factory(question_id=question)
    answer2 = answer_factory(question_id=question)

    serializer = QuestionSerializerWithAnswer(question)
    data = serializer.data
    assert data["id"] == question.id
    assert isinstance(data["text"], str)
    assert len(data["answers"]) == 2


@pytest.mark.django_db
def test_answer_serializer(question_factory, answer_factory):
    question = question_factory()
    answer = answer_factory(question_id=question)
    serializer = AnswerSerializer(answer)
    data = serializer.data
    assert data["id"] == answer.id
    assert data["question_id"] == question.id
    assert isinstance(data["user_id"], str)
    assert isinstance(data["text"], str)
