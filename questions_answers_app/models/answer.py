from django.db import models

from questions_answers_app.models.question import Question


class Answer(models.Model):
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    user_id = models.CharField(max_length=80)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(fields=["-created_at"]),
        ]

    def __str__(self):
        return f"Answer: {self.text} on question: {self.question_id}"
