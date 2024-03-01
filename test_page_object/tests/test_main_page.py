import pytest
from data import Answers


class TestMainPage:

    @pytest.mark.parametrize(
        "num, expected_result",
        [
            (0, Answers.ANSWER_Q0),
            (1, Answers.ANSWER_Q1),
            (2, Answers.ANSWER_Q2),
            (3, Answers.ANSWER_Q3),
            (4, Answers.ANSWER_Q4),
            (5, Answers.ANSWER_Q5),
            (6, Answers.ANSWER_Q6),
            (7, Answers.ANSWER_Q7)
        ]
    )
    def test_questions(self, main_page, num, expected_result):
        assert expected_result == main_page.click_question_and_get_answer_text(num)
