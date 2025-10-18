# filename: main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone

app = FastAPI()

Cat_api = "https://catfact.ninja/fact"

@app.get("/me")
def detaills() -> JSONResponse:
    try:
        response = requests.get(Cat_api, timeout=10)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Cats are mysterious creatures.")
    except requests.RequestException:
        cat_fact = "Could not fetch a cat fact right now. Try again later."

    
    data = {
        "status": "success",
        "user": {
            "email": "kayodejohnson01@gmail.com",
            "name": "Johnson KAYODE",
            "stack": "Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return JSONResponse(content=data, status_code=200)
