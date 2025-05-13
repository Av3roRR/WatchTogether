from fastapi import FastAPI

app = FastAPI(title="Watch Together")


@app.get("/")
async def root():
    return "Привет"