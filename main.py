import os
import fastapi
import uvicorn
from typing import Optional

api = fastapi.FastAPI()


@api.get("/")
def index():
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Ciao PythonBiellaGroup</h1>"
        "</body>"
        "</html>"
    )
    return fastapi.responses.HTMLResponse(content=body)


if __name__ == "__main__":
    port = int(os.environ.get('API_ENDPOINT_PORT', '8000'))
    host = os.environ.get('API_ENDPOINT_HOST', '127.0.0.1')

uvicorn.run('main:api', port=port, host=host, reload=True)