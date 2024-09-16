from fastapi import FastAPI
from app.routers import issues

fastapi = FastAPI()

fastapi.include_router(router=issues.router, prefix='/v1/api')
