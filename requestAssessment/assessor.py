import time

from requests import post


class Assessor:
    def __init__(self, token, refresh):
        self.long_pause = 10
        self.short_pause = 2
        self.retries = 60
        self.token = token
        self.refresh = refresh
        self.response = None

    def ass_request(self):
        res = post(
            url='https://green-lms.app/api/assessments/request',
            json={"pools": [8]},
            headers={"fos-id": "10",
                     "Content-Type": "application/json",
                     },
            cookies={"refresh": self.refresh,
                     "token": self.token},
        )
        # print(res.json())
        self.response = res
        print(f'ass_request result: {res.json()}')
        return res

    def send_requests(self):
        self.ass_request()
        while self.response.status_code in (404, 200) and self.retries > 0:
            print(f'retries left: {self.retries}')
            if self.response.status_code == 404:
                time.sleep(self.short_pause * 60)
            else:
                time.sleep(self.long_pause * 60)
            self.ass_request()
            self.retries -= 1
        print('Program gets over')

    def set_params(self):
        flag = True
        while flag:
            retries = input('\nHow many times do you want to click on "Request" button?\nInput '
                            'number or press Enter if default 60 times are Ok: ')
            try:
                self.retries = int(retries) if retries else self.retries
                flag = False
            except ValueError:
                print('Wrong input')

        print(self.retries)
        flag = True
        while flag:
            short_pause = input(
                '\nHow many minutes do you want to wait until \nclick on "Request" button if "There\'s '
                'no teams"?\nInput '
                'number or press Enter if default 2 minutes are Ok: ')
            try:
                self.short_pause = int(short_pause) if short_pause else self.short_pause
                flag = False
            except ValueError:
                print('Wrong input')
        print(self.short_pause)

        flag = True
        while flag:
            long_pause = input('how many minutes do you want to wait until \nclick on "Request" button if '
                               'someone got found"?\nInput '
                               'number or press Enter if default 10 minutes are Ok: ')
            try:
                self.long_pause = int(long_pause) if long_pause else self.long_pause
                flag = False
            except ValueError:
                print('Wrong input')
        print(self.long_pause)

