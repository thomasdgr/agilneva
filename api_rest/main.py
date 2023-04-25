import os
import logging

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# *****************************************************************************
#                  Some general constants and variables
# *****************************************************************************
NAME = 'Agileneva API'
VERSION = '1.0.0'
DESCRIPTION = 'Agileneva MS for Software Engineering course at HES-SO Master.'
URL_PREFIX: str = os.getenv("URL_PREFIX") or ""
SERVER_ADDRESS: str = os.getenv("SERVER_ADDRESS") or ""
EXPOSED_ADDRESS: str = "https://myserver.com/"

# *****************************************************************************
#                  FastAPI entry point declaration
# *****************************************************************************
rootapp = FastAPI()

app = FastAPI(openapi_url='/specification')
app.add_middleware(CORSMiddleware, allow_origins=["*"], 
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(title=NAME, version=VERSION, 
        description=DESCRIPTION, routes=app.routes,)
    openapi_schema["info"]["x-logo"] = {"url": "assets/logo.png"}
    if SERVER_ADDRESS != "":
        openapi_schema["servers"] = [
            {"url": EXPOSED_ADDRESS + URL_PREFIX, 
            "description": "Agileneva API server"},
        ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
rootapp.mount(URL_PREFIX, app)
logger = logging.getLogger("uvicorn.error")
logger.info('Starting app with URL_PREFIX=' + URL_PREFIX)

# *****************************************************************************
#                  The classes defining the API input and output models
# *****************************************************************************

class obj(BaseModel):
    var: str

# *****************************************************************************
#                  Routes of the API
# *****************************************************************************

@rootapp.on_event("startup")
def startup_event():
    logger.info("Starting up...")
    
@app.get("/")
def info():
    return {'message': 'Welcome to the Agileneva API.'
                       'Try out /showcase for the demo or /docs for the doc.'}

@app.get("/showcase")
def showcase():
    logger.info("route '/showcase' called")
    return FileResponse("./api_rest/showcase/index.html")

@app.get("/assets/{filename}")
async def assets(filename: str):
    logger.info("route '/assets/{}' called".format(filename))
    return FileResponse("./api_rest/showcase/assets/" + filename)

# *****************************************************************************
#                  Utility functions
# *****************************************************************************