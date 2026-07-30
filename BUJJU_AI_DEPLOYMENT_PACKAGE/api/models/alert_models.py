from datetime import datetime
from pydantic import BaseModel

class Alert(BaseModel):
    id: str
    name: str
    severity: str
    status: str
    source: str
    message: str
    created_at: datetime
    metadata: dict = {}
