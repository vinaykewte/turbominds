from fastapi import FastAPI
from api.v1.endpoints import brief

app = FastAPI()

app.include_router(brief.router, prefix="/brief", tags=["brief"])