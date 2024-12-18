import pytest
from fastapi.testclient import TestClient
from Api import app  # Import your FastAPI app test 4

client = TestClient(app)

@pytest.mark.parametrize("number,expected", [
    (1, {"is_prime": False}),
    (2, {"is_prime": True}),
    (3, {"is_prime": True}),
    (4, {"is_prime": False}),
    (5, {"is_prime": True}),
    (10, {"is_prime": False}),
    (13, {"is_prime": True}),
    (17, {"is_prime": True}),
    (19, {"is_prime": True}),
    (20, {"is_prime": False}),
])
def test_check_prime(number, expected):
    response = client.get(f"/check_prime/{number}")
    assert response.status_code == 200
    assert response.json() == expected
