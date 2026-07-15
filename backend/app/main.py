from fastapi import FastAPI

app = FastAPI(
    title = "Proinventory API",
    version = "1.00",
)

app.get("/")
def root():
    return {
        "message": "Welcome to the backend"
}