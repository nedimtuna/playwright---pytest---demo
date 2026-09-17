import os

import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        api_key = os.getenv("REQRES_API_KEY")

        if api_key:
            self.session.headers.update({
                "x-api-key": api_key
            })

    def get(self, endpoint):
        return self.session.get(
            self._build_url(endpoint),
            timeout=10,
        )

    def post(self, endpoint, payload):
        return self.session.post(
            self._build_url(endpoint),
            json=payload,
            timeout=10,
        )

    def put(self, endpoint, payload):
        return self.session.put(
            self._build_url(endpoint),
            json=payload,
            timeout=10,
        )

    def patch(self, endpoint, payload):
        return self.session.patch(
            self._build_url(endpoint),
            json=payload,
            timeout=10,
        )

    def delete(self, endpoint):
        return self.session.delete(
            self._build_url(endpoint),
            timeout=10,
        )

    def _build_url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"