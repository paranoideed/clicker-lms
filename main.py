# main.py
from pathlib import Path
from login.login import Login
from requestAssessment.assessor import Assessor

if __name__ == '__main__':
    auth = Login()  # читает creds.json
    token = auth.get_token()
    refresh = auth.get_refresh()
    if not token or not refresh:
        raise RuntimeError("Missing cookies 'token'/'refresh' after login")

    assessor = Assessor(token, refresh, Path('config.json'))
    assessor.send_requests()
