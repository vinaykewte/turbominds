from uuid import uuid4
from fastapi import APIRouter, HTTPException, Path
from schemas.research import GenerateResearch
from services.research import generate_research, get_research_status
from pydantic import UUID4

router = APIRouter(tags=['research'])

@router.post("")
async def create_research(data: GenerateResearch):
    print("Researching...", data)
    res = generate_research(data)
    return res

@router.get("/{research_id}")
async def get_research(research_id: UUID4 = Path(..., description="Id of research which needs to be extracted")):
    res = get_research_status(research_id)
    return res

