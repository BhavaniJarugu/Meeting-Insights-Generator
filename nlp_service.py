class NLPService:

    def keywords(self,text):
        return text.split()[:10]

    def sentiment(self,text):
        return 'Neutral'

    def entities(self,text):
        return []
