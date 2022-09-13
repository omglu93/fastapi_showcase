from fastapi import FastAPI
from app.core.config import settings
import uvicorn

from app.api.api_v1 import api

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api.router, prefix=settings.API_VERSION)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)