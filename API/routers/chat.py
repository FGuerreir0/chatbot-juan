from fastapi import APIRouter, Response, status as fastapi_status
from util.fn import juan_profile_responds
from pydantic import BaseModel
import logging

logger = logging.getLogger("JUAN:API")

router = APIRouter()

class ChatRequest(BaseModel):
    userInput: str
    isProfile: bool = False

@router.post("/juan/profile/chat")
async def send_chat_message(chat_request: ChatRequest, response: Response):
    try:
        userInput = chat_request.userInput
        isProfile = chat_request.isProfile
        logger.info(f"User Input: {userInput}, Is Profile Context: {isProfile}")
        chatbot_response = await juan_profile_responds(userInput, isProfile)
        return {
            "input": userInput,
            "response": chatbot_response,
        }, fastapi_status.HTTP_200_OK
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        response.status_code = 500
        return {"status": "Error", "error": str(e)}