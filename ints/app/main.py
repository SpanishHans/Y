import uvicorn
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# 
from rutas.interacciones import router
from conf.database import engine
from modelos import modelos

modelos.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Servicio de Interacciones",
    description="API para gestión de likes y comentarios",
    version="1.0.0"
)

# # Configuración CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Incluir rutas
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Servicio de Interacciones activo"}

# # Para ejecutar con un puerto específico
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)