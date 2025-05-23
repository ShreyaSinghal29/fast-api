from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": a * b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.apiserver:app", host="127.0.0.1", port=8000,reload=False)