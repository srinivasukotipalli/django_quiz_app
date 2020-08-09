import pytest
from quiz.models import Quiz, Progress, Category, Question

@pytest.mark.django_db
def test_quiz_creation(create_quiz):
    quiz_obj = Quiz.objects.get(id=1)
    actual_output = quiz_obj.title
    expected_output = "test title"
    assert expected_output == actual_output

@pytest.mark.django_db
def test_progress_creation(create_progress):
    progress_obj = Progress.objects.get(id=1)
    actual_output = progress_obj.correct_answer
    expected_output = "correct"
    assert expected_output == actual_output

@pytest.mark.django_db
def test_category(create_category):
    category_obj = Category.objects.get(id=1)
    actual_output = category_obj.category
    expected_output = "C"
    assert expected_output == actual_output

@pytest.mark.django_db
def test_question(create_question):
    question_obj = Question.objects.get(id=1)
    actual_output = question_obj.content
    expected_output = "ques"
    assert expected_output == actual_output



