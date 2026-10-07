from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Banking",
    description="Fully featured banking application built with FastAPI",
)

@app.get("/")
def home():
    return {"message": "Welcome to my fastAPI banking app"}