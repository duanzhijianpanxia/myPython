import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''
    def test_store_single_response(self):
        '''测试单个答案也会被妥善存储'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("Chinese")

        self.assertIn('Chinese', my_survey.responses)


    def test_store_three_responses(self):
        '''测试三个答案也会被妥善存储'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Chinese', 'Franch']
        for response in responses:
            my_survey.store_response(response)
            # 定义三个不同答案的类表，并调用存储函数将其存储

        for response in responses:
            self.assertIn(response, my_survey.responses)
            # 将上面的结果和方法结果做判断，是否在列表中

if __name__ == "__main__":
    unittest.main()