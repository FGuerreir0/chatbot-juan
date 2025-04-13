from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)