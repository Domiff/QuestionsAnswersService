FROM python:3.12-slim

ENV POETRY_VERSION=1.8.0 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["gunicorn", "questions_answers_project.wsgi:application", "--bind", "0.0.0.0:8000"]