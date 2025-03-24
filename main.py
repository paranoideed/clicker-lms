# pip install - r requirements.txt

from login.login import Login
from requestAssessment.assessor import Assessor

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    logining_result = Login()
    # print(logining_result.get_token())
    assessor_result = Assessor(logining_result.get_token(), logining_result.get_refresh())
    assessor_result.set_params()
    assessor_result.send_requests()

    # pass