# requestAssessment/assessor.py
import time
import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from requests import post

cr = Path('config.json')

def _load_creds(path: Path) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

class Assessor:
    def __init__(self, token: str, refresh: str, creds_path: Path = cr):
        data = _load_creds(creds_path)
        cfg = (data.get("assessor") or {})

        self.retries: int = int(cfg.get("retries", ))
        self.short_pause: int = int(cfg.get("short_pause_sec", 2))
        self.long_pause: int = int(cfg.get("long_pause_sec", 10))
        self.pools: List[int] = list(cfg.get("pools", [16]))
        self.fos_id: str = str(cfg.get("fos_id", "23"))

        self.token = token
        self.refresh = refresh
        self.response = None

    def ass_request(self):
        res = post(
            url='https://green-lms.app/api/assessments/request',
            json={"pools": self.pools},
            headers={
                "fos-id": self.fos_id,
                "Content-Type": "application/json",
            },
            cookies={
                "refresh": self.refresh,
                "token": self.token
            },
        )
        self.response = res
        try:
            print(f'ass_request result: {res.status_code} | {res.json()}')
        except Exception:
            print(f'ass_request result: {res.status_code} | {res.text}')
        return res

    def send_requests(self):
        # первый запрос
        self.ass_request()
        attempts_left = self.retries

        while self.response is not None and self.response.status_code in (200, 404) and attempts_left > 0:
            print(f'retries left: {attempts_left}')
            pause = self.short_pause if self.response.status_code == 404 else self.long_pause
            time.sleep(pause)
            self.ass_request()
            attempts_left -= 1

        print('Program gets over')
