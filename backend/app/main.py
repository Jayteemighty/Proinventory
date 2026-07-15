from fastapi import FastAPI

app = FastAPI(
    title="ProInventory API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ProInventory API"
    }