from pydantic import BaseModel

class TranscriptRequest(BaseModel):
    transcript:str

class SummaryResponse(BaseModel):
    summary:str

class ActionItemResponse(BaseModel):
    actions:list[str]

class DecisionResponse(BaseModel):
    decisions:list[str]
