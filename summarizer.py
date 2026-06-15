class Summarizer:

    def generate(self,text):
        return text[:300]

    def executive_summary(self,text):
        return text[:150]

    def detailed_summary(self,text):
        return text[:500]
