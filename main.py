from fastapi import FastAPI

app = FastAPI()

@app.get(path="/")
def home():
    return {"Twitter": "Working!"}