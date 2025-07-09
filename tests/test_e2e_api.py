from clients.calculator_client import CalculatorClient


def test_get_sum(calculator_client: CalculatorClient):
    response = calculator_client.get_sum(a=1, b=2)
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_get_double_sum(calculator_client: CalculatorClient):
    response = calculator_client.get_double_sum(a=1, b=2)
    assert response.status_code == 200
    assert response.json() == {"result": 6}
