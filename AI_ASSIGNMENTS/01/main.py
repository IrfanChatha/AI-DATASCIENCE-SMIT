from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def create_user(id: str, name: str):
    return {
        "status": "success",
        "data": {
            "id": id,
            "name": name
        }
    }
