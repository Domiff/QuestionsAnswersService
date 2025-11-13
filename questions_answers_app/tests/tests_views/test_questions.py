import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_get_all_question(api_client, question_factory):
    question_factory()
    question_factory()
    question_factory()
    url = reverse("questions_answers_app:questions")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_crete_question(api_client, question_factory):
    data = {"text": question_factory().text}
    url = reverse("questions_answers_app:create_question")
    response = api_client.post(url, data=data)
    assert response.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_get_one_question(api_client, question_factory):
    question = question_factory()
    url = reverse("questions_answers_app:question", args=[question.id])
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_delete_question(api_client, question_factory):
    question = question_factory()
    url = reverse("questions_answers_app:delete_question", args=[question.id])
    response = api_client.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT
