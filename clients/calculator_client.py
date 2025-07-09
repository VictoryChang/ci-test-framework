from requests import Response
from requests_toolbelt.sessions import BaseUrlSession


class CalculatorClient:
    def __init__(self):
        self.session = BaseUrlSession("http://127.0.0.1:8000")

    def get_sum(self, a: int, b: int) -> Response:
        return self.session.get("/api/sum", params={"a": a, "b": b})

    def get_double_sum(self, a: int, b: int) -> Response:
        return self.session.get("/api/double_sum", params={"a": a, "b": b})
