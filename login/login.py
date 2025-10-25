# login/login.py
import json
from pathlib import Path
from requests import post

cr = Path('creds.json')

class Login:
    def __init__(self, creds_path: Path = cr):
        self.creds_path = creds_path
        self.creds = self._get_creds()
        self.response = self._authorize()
        if self.response.status_code != 200:
            raise RuntimeError(
                f'Login failed: status={self.response.status_code}, body={self.response.text}'
            )

    def _get_creds(self):
        with open(self.creds_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        login = data.get("login")
        password = data.get("password")
        if not login or not password:
            raise ValueError("Missing 'login' or 'password' in creds.json")
        return {"login": login, "password": password}

    def _authorize(self):
        return post(
            url='https://green-lms.app/api/login',
            json=self.creds,
            headers={"Content-Type": "application/json"},
        )

    def get_token(self):
        return self.response.cookies.get_dict().get('token')

    def get_refresh(self):
        return self.response.cookies.get_dict().get('refresh')
