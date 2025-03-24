import json
from pathlib import Path
from requests import post

from pprint import pprint

cr = Path('creds.json')


class Login:

    def __init__(self, creds=cr):
        self.cr = creds
        self.creds = self.get_creds()
        while True:
            self.response = self.authorize()
            if self.response.status_code == 200:
                print('logining successful\n')
                break
            else:
                print(f'logining failed!!!!!\n'
                      f'status_code: {self.response.status_code}\n'
                      f'response body: {self.response.json()}')
                input('check your login and password in creds.json or be careful inputting them\n'
                      'press Enter to continue')
                self.creds = self.get_creds()

    def get_creds(self):
        with open(self.cr, 'r') as file:
            creds = json.load(file)
        if creds["login"]:
            login = creds["login"]
        else:
            login = input('input login: ')
        if creds["password"]:
            password = creds["password"]
        else:
            password = input('input password: ')
        return {
            'login': login,
            'password': password,
        }

    def authorize(self):
        res = post(
            url='https://green-lms.app/api/login',
            json=self.creds,
            headers={"Content-Type": "application/json"},
        )
        return res

    def get_token(self):
        return self.response.cookies.get_dict()['token']

    def get_refresh(self):
        return self.response.cookies.get_dict()['refresh']


# a = Login()
# print(a.get_token())
# print(a.get_refresh())

