from uuid import uuid4
from fastapi import APIRouter, HTTPException, Path, Header
from schemas.blueprint import BlueprintAdd, BlueprintCreate, BlueprintResponse, BlueprintUpdate
from services.blueprint import BlueprintService
from pydantic import UUID4

router = APIRouter(prefix="/blueprint", tags=["blueprint"])

@router.post("/{blueprint_id}", response_model=BlueprintResponse)
async def create_blueprint(blueprint_id: str, blueprint: BlueprintCreate, x_company_id: str = Header(...)):
    return BlueprintService.create_blueprint(blueprint_id, blueprint, x_company_id)

@router.put("/{blueprint_id}", response_model=BlueprintResponse)
async def update_blueprint(blueprint_id: str, blueprint: BlueprintUpdate, x_company_id: str = Header(...)):
    return BlueprintService.update_blueprint(blueprint_id, blueprint, x_company_id)

@router.post("/add-to-blueprint/{blueprint_id}", response_model=BlueprintResponse)
async def add_to_blueprint(blueprint_id: str, blueprint: BlueprintAdd, x_company_id: str = Header(...)):
    return BlueprintService.add_to_blueprint(blueprint_id, blueprint, x_company_id)

@router.get("/{blueprint_id}", response_model=BlueprintResponse)
async def get_blueprint(blueprint_id: str, x_company_id: str = Header(...)):
    return BlueprintService.get_blueprint(blueprint_id, x_company_id)

@router.get("/", response_model=list[BlueprintResponse])
async def list_blueprints(x_company_id: str = Header(...)):
    return BlueprintService.list_blueprints(x_company_id)

@router.get("/{blueprint_id}/download")
async def download_blueprint(blueprint_id: str, x_company_id: str = Header(...)):
    return BlueprintService.download_blueprint(blueprint_id, x_company_id)