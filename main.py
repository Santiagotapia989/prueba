from fastapi import FastAPI
import os

app = FastAPI()

# Endpoint principal
@app.get("/")
def home():
    return {"mensaje": "API funcionando 🚀"}

# Nuevo endpoint
@app.get("/saludo")
def saludo():
    return {"mensaje": "Hola desde Railway 🚀"}

# Endpoint con variable de entorno
@app.get("/config")
def config():
    return {"app": os.getenv("APP_NAME")}