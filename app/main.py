from fastapi import FastAPI
from .api.routes import router
from .core.logging import logger

app = FastAPI(title="Wati Webhook Service")

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Wati webhook service")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)