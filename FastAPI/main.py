from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/url")
async def url():
    return {"url": "https://github.com/braiso-22/python-backend"}
