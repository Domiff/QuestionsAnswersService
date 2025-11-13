import pytest
from rest_framework.test import APIClient

from .factories import QuestionFactory, AnswerFactory


@pytest.fixture
def question_factory():
    return QuestionFactory


@pytest.fixture
def answer_factory():
    return AnswerFactory


@pytest.fixture
def api_client():
    return APIClient()
