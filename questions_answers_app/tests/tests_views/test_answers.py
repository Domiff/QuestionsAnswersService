import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_create_answer(api_client, question_factory):
    question = question_factory()
    data = {
        "text": "ggbtf",
        "user_id": "testuser",
        "question_id": question.id

    }
    url = reverse("questions_answers_app:create_answer", args=[question.id])
    response = api_client.post(url, data=data)

    assert response.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_get_answer(api_client, question_factory, answer_factory):
    question = question_factory()
    answer = answer_factory(question_id=question)
    url = reverse("questions_answers_app:get_answer", args=[answer.id])
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_delete_answer(api_client, question_factory, answer_factory):
    question = question_factory()
    answer = answer_factory(question_id=question)
    url = reverse("questions_answers_app:delete_answer", args=[answer.id])
    response = api_client.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT
