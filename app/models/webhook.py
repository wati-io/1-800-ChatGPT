from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WatiMessage(BaseModel):
    id: str
    created: str
    whatsappMessageId: Optional[str]
    conversationId: str
    ticketId: str
    text: Optional[str]
    type: str
    data: Optional[str] = None
    timestamp: str
    owner: bool
    eventType: str
    statusString: Optional[str]
    waId: str
    senderName: str