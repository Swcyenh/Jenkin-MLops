import requests

link = "http://127.0.0.1:80"

def test_check_prime_1():
    response = requests.get(f"{link}/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_check_prime_2():
    response = client.get("/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_check_prime_3():
    response = client.get("/check_prime/3")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_check_prime_4():
    response = client.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_check_prime_5():
    response = client.get("/check_prime/5")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_check_prime_10():
    response = client.get("/check_prime/10")
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}

def test_check_prime_11():
    response = client.get("/check_prime/11")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_check_prime_13():
    response = client.get("/check_prime/13")
    assert response.status_code == 200
    assert response.json() == {"is_prime": True}

def test_check_prime_15():
    response = client.get("/check_prime/15")
    assert response.status_code == 200
    assert response.json() == {"is_prime": False}