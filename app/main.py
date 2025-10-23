from fastapi import FastAPI

app = FastAPI(title="Transportes Sigmotoa API")

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a Transportes Sigmotoa "}
