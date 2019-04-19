'''在前面的test_survey.py中，我们在每一个方法中都创建了一个AnonymousSurvey实例，
并在每个方法中都创建了答案。unittest.TestCase类包含方法setup(),python 将先运行它，再运行各个
以test打头的方法。这样你在编写的每个方法中都可以使用在方法setUp（）中创建的对象了

下面将利用setUp（）方法创建一个问题和一组答案，供方法test_store_single_response()和
方法test_store_three_response()使用'''

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    # 针对AnonymousSuvery类的测试

    def setUP(self):
        # 创建一个调查对象和一组答案
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Franch']

    def test_store_single_response(self):
        # 测试单个答案也能被妥善的保存
        self.my_survey .store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        # 测试三个答案会被妥善保存
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()