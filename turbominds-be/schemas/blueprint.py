from pydantic import BaseModel
from typing import List

class BlueprintCreate(BaseModel):
    final_brief: str

class BlueprintUpdate(BaseModel):
    final_brief: str
    images: List[str]

class BlueprintAdd(BaseModel):
    result: str

class BlueprintResponse(BaseModel):
    id: str
    final_brief: str
    images: List[str]
    updated_at: str