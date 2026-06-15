class ActionItemExtractor:

    def extract(self,text):
        actions=[]
        for line in text.split('.'):
            if 'will' in line.lower():
                actions.append(line.strip())
        return actions

    def count(self,text):
        return len(self.extract(text))
