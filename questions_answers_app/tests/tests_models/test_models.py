import pytest


@pytest.mark.django_db
def test_question(question_factory):
    question = question_factory()
    assert isinstance(question.text, str)


@pytest.mark.django_db
def test_answer(answer_factory):
    answer = answer_factory()
    assert isinstance(answer.text, str)
    assert isinstance(answer.user_id, str)
