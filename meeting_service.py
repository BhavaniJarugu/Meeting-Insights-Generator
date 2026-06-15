from summarizer import Summarizer
from action_item_extractor import ActionItemExtractor

class MeetingService:

    def __init__(self):
        self.summarizer = Summarizer()
        self.extractor = ActionItemExtractor()

    def analyze(self, transcript):
        return {
            'summary': self.summarizer.generate(transcript),
            'actions': self.extractor.extract(transcript)
        }
