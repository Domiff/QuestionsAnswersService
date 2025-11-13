import factory

from questions_answers_app.models import Question, Answer


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    text = factory.Faker("text")


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer

    question_id = factory.SubFactory(QuestionFactory)
    user_id = factory.Faker("sentence")
    text = factory.Faker("text")
