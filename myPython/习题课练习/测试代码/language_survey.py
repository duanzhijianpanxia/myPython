from survey import AnonymousSurvey
# 定义一个问题，并创建一个表示AnonymousSurvey对象
question = 'What language did you first learn to speak ? '
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey .show_question()
print("Enter  'q' anytime to quit")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# 显示调查结果
print("thrank you to everyone who participated in the survey!")
my_survey.show_results()