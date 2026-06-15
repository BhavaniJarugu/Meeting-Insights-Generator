class DecisionExtractor:

    def extract(self,text):
        decisions=[]
        for line in text.split('.'):
            if 'decided' in line.lower():
                decisions.append(line.strip())
        return decisions

    def total(self,text):
        return len(self.extract(text))
