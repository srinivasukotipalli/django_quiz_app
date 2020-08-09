import pytest
from quiz.models import Quiz, Category, User, Progress, Question


@pytest.fixture()
def create_user():
    user = User(username="srinu", email="srinivasktpl1222@gmail.com",
                is_staff=True, is_active=True)
    user.set_password("1234")
    user.save()
    return user

@pytest.fixture()
def create_question():
    question_obj = Question.objects.create(content="ques")
    return question_obj

@pytest.fixture()
def create_category():
    category = Category.objects.create(category="C")
    return category

@pytest.fixture()
def create_quiz(create_category):
    quiz_obj = Quiz.objects.create(
        title="test title",
        description="hi This is test description.....",
        url = "hai",
        category_id = 1,
        random_order = True,
        max_questions = 2,
        answers_at_end = True,
        exam_paper = True,
        single_attempt = True,
        pass_mark = 2,
        success_text = "passed",
        fail_text = "Fail",
        draft = False
    )
    return quiz_obj


@pytest.fixture()
def create_progress(create_user):
    progress_obj = Progress.objects.create(
                            user_id = 1,
                            score = "score",
                            correct_answer = "correct",
                            wrong_answer = "wrong"
                    )
    return progress_obj
