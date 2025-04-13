import argparse
from routers import chat
import logger as Logger
from fastapi import FastAPI
from util.fn import Start_LLM
import uvicorn
from routers import status

logger = Logger.setup("JUAN:API")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', type=str, help='Host')
    parser.add_argument('-p', '--port', default=8051, type=int, help='Port to run the app on')
    return parser.parse_args()

args = get_args()

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    Start_LLM()
    routes = [route.path for route in app.routes]
    logger.info(f"Registered routes: {routes}")

app.include_router(status.router)
app.include_router(chat.router)

if __name__ == "__main__":
    try:
        logger.info(f"Starting JUAN ChatBot API")
        uvicorn.run(app, host=args.host, port=int(args.port))
    except Exception as e:
        logger.error(f"Error: {e}")