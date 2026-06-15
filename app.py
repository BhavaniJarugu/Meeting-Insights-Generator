from fastapi import FastAPI
from schemas import TranscriptRequest
from meeting_service import MeetingService

app = FastAPI(title='Meeting Insights Generator')
service = MeetingService()

@app.get('/health')
def health():
    return {'status':'healthy'}

@app.post('/analyze')
def analyze(req: TranscriptRequest):
    return service.analyze(req.transcript)
