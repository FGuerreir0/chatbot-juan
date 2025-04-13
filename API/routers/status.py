from fastapi import APIRouter, Response, status as fastapi_status
import logging

logger = logging.getLogger("JUAN:API")

router = APIRouter()

@router.get("/status")
async def get_status(response: Response):
    try:
        logger.info("Status endpoint hit")
        return {"status": "OK", "name": "JUAN ChatBot API"}
    except Exception as e:
        logger.error(f"Error: {e}")
        response.status_code = fastapi_status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "Error", "error": str(e)}