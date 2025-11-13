from django.urls import path

from .views import (
    GetAllQuestion,
    CreateQuestion,
    GetOneQuestion,
    DeleteQuestion,
    GetAnswer,
    CreateAnswer,
    DeleteAnswer,
)

app_name = "questions_answers_app"


urlpatterns = [
    path("questions/", GetAllQuestion.as_view(), name="questions"),
    path("questions/create", CreateQuestion.as_view(), name="create_question"),
    path("questions/<int:id>", GetOneQuestion.as_view(), name="question"),
    path("questions/delete/<int:id>", DeleteQuestion.as_view(), name="delete_question"),
    path("questions/<int:id>/answers", CreateAnswer.as_view(), name="create_answer"),
    path("answers/<int:id>", GetAnswer.as_view(), name="get_answer"),
    path("answers/delete/<int:id>", DeleteAnswer.as_view(), name="delete_answers"),
]
