from dataclasses import dataclass

@dataclass
class Meeting:
    title:str
    transcript:str

@dataclass
class ActionItem:
    description:str

@dataclass
class Decision:
    text:str
