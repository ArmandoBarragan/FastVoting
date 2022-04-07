from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    pass


# Authentication
@app.post("/users/signup")
def sign_up():
    pass


@app.post("users/login")
def login():
    pass
