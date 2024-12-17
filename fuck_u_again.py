import requests

link = "http://127.0.0.1:80"

def test_check_prime_2():
    response = requests.get(f"{link}/check_prime/2")
    print(response.json()== {"is_prime": True})
    return response.json() == {"is_prime": True}

def test_check_prime_3():
    response = requests.get(f"{link}/check_prime/3")
    print(response.json()== {"is_prime": True})
    return response.json() == {"is_prime": True}

def test_check_prime_4():
    response = requests.get(f"{link}/check_prime/4")
    print(response.json()== {"is_prime": False})
    return response.json() == {"is_prime": False}

def test_check_prime_5():
    response = requests.get(f"{link}/check_prime/5")
    print(response.json()== {"is_prime": True})
    return response.json() == {"is_prime": True}

def test_check_prime_6():
    response = requests.get(f"{link}/check_prime/6")
    print(response.json()== {"is_prime": False})
    return response.json() == {"is_prime": False}

def test_check_prime_7():
    response = requests.get(f"{link}/check_prime/7")
    print(response.json()== {"is_prime": True})
    return response.json() == {"is_prime": True}

def test_check_prime_8():
    response = requests.get(f"{link}/check_prime/8")
    print(response.json()== {"is_prime": False})
    return response.json() == {"is_prime": False}

def test_check_prime_9():
    response = requests.get(f"{link}/check_prime/9")
    print(response.json()== {"is_prime": False})
    return response.json() == {"is_prime": False}

def test_check_prime_10():
    response = requests.get(f"{link}/check_prime/10")
    print(response.json()== {"is_prime": False})
    return response.json() == {"is_prime": False}

def test_check_prime_11():
    response = requests.get(f"{link}/check_prime/11")
    print(response.json()== {"is_prime": True})
    return response.json() == {"is_prime": True}


