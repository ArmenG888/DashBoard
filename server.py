# simple fast api app

from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def read_item():
    with open("test.txt", "r") as r:
    	throttle = r.read()
    return {'thorttle':throttle}

