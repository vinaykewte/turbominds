from uuid import uuid4
from fastapi import APIRouter, HTTPException, Path
from schemas.strategy import GenerateStrategy
from services.strategy import generate_strategy, get_strategy_status
from pydantic import UUID4

router = APIRouter(tags=['strategy'])

@router.post("")
async def create_strategy(data: GenerateStrategy):
    print("Strategising...", data)
    res = generate_strategy(data)
    return res

@router.get("/{strategy_id}")
async def get_strategy(strategy_id: UUID4 = Path(..., description="Id of strategy which needs to be extracted")):
    res = get_strategy_status(strategy_id)
    return res

