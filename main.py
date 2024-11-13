import logging
import os

from fastapi import FastAPI

from routes import health_check

log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    _app = FastAPI(title="Restaurant Service", version="1.0.0")
    _app.include_router(health_check.router, prefix="/health", tags=["health_check"])
    return _app


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up....")

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")