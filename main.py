
from fastapi import FastAPI

app = FastAPI()  # Create FastAPI application instance


@app.get("/")
def read_root():
    return {"message": "Welcome to GenAI API!"}


@app.get("/generate/{prompt}")
def generate_text(prompt: str, max_tokens: int = 100):
    return {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "response": f"Generated text for: {prompt}"
    }
