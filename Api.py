from fastapi import FastAPI
from typing import Dict
import uvicorn

app = FastAPI()

@app.get("/get_version")
def get_version() -> Dict[str, str]:
    return {"version": "1.0.0"}

@app.get("/check_prime/{number}")
def check_prime(number: int) -> Dict[str, bool]:
    if number < 2:
        return {"is_prime": False}
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}

@app.get("/get_fibonacci/{number}")
def get_fibonacci(number: int) -> Dict[str, int]:
    if number < 0:
        return {"error": "Number must be non-negative"}
    a, b = 0, 1
    for _ in range(number):
        a, b = b, a + b
    return {"fibonacci": a}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)