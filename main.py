import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel

from config.settings import settings
from utils.normalizer import normalize_text
from utils.scorer import score_intents, decide_action


logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(settings.APP_NAME)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing %s...", settings.APP_NAME)
    logger.info("Running in %s mode", "DEBUG" if settings.DEBUG else "PRODUCTION")

    if settings.API_KEY:
        logger.info("API Key detected")
    else:
        logger.warning("API Key not found; app running with limited functionality")

    yield

    logger.info("Shutting down %s...", settings.APP_NAME)


app = FastAPI(
    title=settings.APP_NAME,
    version="3.6",
    lifespan=lifespan,
)


class DispatchRequest(BaseModel):
    query: str


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": "3.6",
    }


@app.post("/dispatch")
async def dispatch(request: DispatchRequest):
    original_query = request.query
    normalized_query = normalize_text(original_query)
    scores = score_intents(normalized_query)
    decision = decide_action(scores)

    logger.info(
        "dispatch_decision | query=%s | normalized=%s | scores=%s | action=%s",
        original_query,
        normalized_query,
        scores,
        decision["recommended_action"],
    )

    return {
        "input": original_query,
        "normalized_input": normalized_query,
        "decision": decision,
    }
