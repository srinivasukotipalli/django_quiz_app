import pytest
from mcq.models import MCQQuestion, Answer

@pytest.fixture()
def create_mcqQuestion():
    mcq_obj = MCQQuestion.objects.create(answer_order="content", content="hi hello", explanation="this is robo")
    return mcq_obj

@pytest.fixture()
def create_answer(create_mcqQuestion):
    ans_obj = Answer.objects.create(question_id = 1,content = "Dennis Ritchie",correct = True)
    return ans_obj


