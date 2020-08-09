import pytest
from mcq.models import MCQQuestion, Answer

@pytest.mark.django_db
def test_mcqQuestion_creation(create_mcqQuestion):
    MCQQuestion_obj = MCQQuestion.objects.get(id=1)
    actual_output = MCQQuestion_obj.answer_order
    expected_output = "content"
    assert expected_output == actual_output

@pytest.mark.django_db
def test_answer_creation(create_answer):
    answer_obj = Answer.objects.get(id=1)
    actual_output = answer_obj.content
    expected_output = "Dennis Ritchie"
    assert expected_output == actual_output




