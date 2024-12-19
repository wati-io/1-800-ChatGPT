from fastapi import APIRouter, HTTPException
from ..models.webhook import WatiMessage
from ..services.wati import WatiService
from ..core.logging import logger

router = APIRouter()
wati_service = WatiService()

@router.post("/webhook/wati")
async def wati_webhook(message: WatiMessage):
    try:
        logger.info(f"Received webhook: {message}")
        
        if message.eventType == "message":
            logger.info(f"Processing message event from {message.waId}")
            response = await wati_service.process_and_reply(
                message.waId,
                message.text
            )
            logger.info(f"Successfully processed message: {response}")
            return {"status": "success", "response": response}
            
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))