from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.admin import router as AdminRouter
from routes.contact import router as ContactRouter

# Inicializar la aplicación FastAPI
app = FastAPI()

# Configurar el listener de token JWT
token_listener = JWTBearer()

# Definir el lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    await initiate_database()
    yield
    # Aquí podrías agregar la lógica de limpieza si fuera necesario

# Crear la instancia de FastAPI con el lifespan
app = FastAPI(lifespan=lifespan)

# Definir una ruta raíz
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}

# Incluir routers para administradores y estudiantes
app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(ContactRouter, tags=["Contacts"], prefix="/contact", dependencies=[Depends(token_listener)])
