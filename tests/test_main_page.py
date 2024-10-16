import pytest

from pages.main_page import MainPage
from data import AnswerText, QuestionText, Url

# Todo: тайтлы и описание для тестов в allure
class TestMainPage:

    @pytest.mark.parametrize('num, question_text, answer_text',
                             [
                                 (0, QuestionText.QUESTION_1, AnswerText.ANSWER_1),
                                 (1, QuestionText.QUESTION_2, AnswerText.ANSWER_2),
                                 (2, QuestionText.QUESTION_3, AnswerText.ANSWER_3),
                                 (3, QuestionText.QUESTION_4, AnswerText.ANSWER_4),
                                 (4, QuestionText.QUESTION_5, AnswerText.ANSWER_5),
                                 (5, QuestionText.QUESTION_6, AnswerText.ANSWER_6),
                                 (6, QuestionText.QUESTION_7, AnswerText.ANSWER_7),
                                 (7, QuestionText.QUESTION_8, AnswerText.ANSWER_8)
                             ]
                             )
    def test_question_and_answers(self, connection, num, question_text, answer_text):
        connection.get(Url)
        main_page = MainPage(connection)
        assert (main_page.get_answer_and_question_text(num)[0] == question_text and
                main_page.get_answer_and_question_text(num)[1] == answer_text)
