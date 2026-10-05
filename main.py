from fastapi import FastAPI

app = FastAPI()

@app.get("/teste")
async def ping():
    return{"mensagem": "HelloWorld!"}