from pydantic import BaseModel

class Message(BaseModel):
    note_id: int
    content: str