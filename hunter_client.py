from typing import Any, Dict

import requests

class HunterClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.hunter.io"

    def verify_email(self, email: str) -> Dict[str, Any]:
        endpoint = f"{self.base_url}/email-verifier"
        params = {"email": email, "api_key": self.api_key}
        response = requests.get(endpoint, params=params)
        return response.json()

class EmailVerificationService:
    def __init__(self):
        self.results = []

    def save_result(self, email: str, result: Dict[str, Any]) -> None:
        self.results.append({"email": email, "result": result})

    def get_results(self) -> Dict[str, Any]:
        return self.results

    def clear_results(self) -> None:
        self.results = []
