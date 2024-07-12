from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, UUID4


class GenerateBrief(BaseModel):
    content: str

class ResGenerateBrief(BaseModel):
    brief_id: UUID4

class BriefEvents(BaseModel):
    status: str
    timestamp: datetime

class ResultQuestions(BaseModel):
    id: UUID4
    question: str
    topic: str

class AllQuestions(BaseModel):
    questions: List[ResultQuestions]

class BriefResult(BaseModel):
    final_brief: str
    questions: AllQuestions

class BriefModel(BaseModel):
    brief_id: UUID4
    events : List[BriefEvents]
    result: Optional[BriefResult] = None