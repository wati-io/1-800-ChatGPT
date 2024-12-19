from httpx import AsyncClient
from ..core.config import settings
from ..core.logging import logger
from openai import AsyncOpenAI

class WatiService:
    def __init__(self):
        self.base_url = settings.WATI_API_URL
        self.headers = {
            "Authorization": f"Bearer {settings.WATI_API_KEY}",
            "Content-Type": "application/json"
        }
        self.ai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def get_ai_response(self, user_message: str) -> str:
        try:
            response = await self.ai_client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error getting AI response: {str(e)}")
            raise

    async def process_and_reply(self, whatsapp_number: str, user_message: str):
        try:
            # Get AI response
            ai_response = await self.get_ai_response(user_message)
            
            # Send response back through Wati
            return await self.send_message(whatsapp_number, ai_response)
        except Exception as e:
            logger.error(f"Error in process_and_reply: {str(e)}")
            raise

    async def send_message(self, whatsapp_number: str, message: str):
        async with AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/api/v1/sendSessionMessage/{whatsapp_number}",
                    headers=self.headers,
                    params={"messageText": message}
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Error sending message: {str(e)}")
                raise