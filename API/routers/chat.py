from fastapi import APIRouter, Response, status as fastapi_status
from util.fn import juan_responds
from pydantic import BaseModel
import logging

logger = logging.getLogger("JUAN:API")

router = APIRouter()

class ChatRequest(BaseModel):
    userInput: str

@router.post("/juan/chat")
async def send_chat_message(chat_request: ChatRequest, response: Response):
    try:
        userInput = chat_request.userInput
        logger.info(f"User input: {userInput}")
        chatbot_response = juan_responds(userInput)
        #logger.info(f"Chatbot response: {chatbot_response}")
        return {"input": userInput, "response": chatbot_response, "status": "200"}
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        response.status_code = 500
        return {"status": "Error", "error": str(e)}

