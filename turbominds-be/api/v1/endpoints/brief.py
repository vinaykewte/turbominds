from uuid import uuid4
from fastapi import APIRouter, HTTPException, Path
from schemas.brief import ResGenerateBrief, GenerateBrief, BriefModel
from services.brief import generate_brief, get_brief_status
from pydantic import UUID4

router = APIRouter()

@router.post("", response_model=ResGenerateBrief)
async def create_brief(content: GenerateBrief):
    print("creating brief...", content)
    res = generate_brief(content)
    return res

@router.get("/{brief_id}", response_model=BriefModel)
async def get_brief(brief_id: UUID4 = Path(..., description="Id of brief which needs to be extracted")):
    # print("getting brief...", brief_id)
    res = get_brief_status(brief_id)
    return res

