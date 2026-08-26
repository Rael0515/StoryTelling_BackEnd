from fastapi import FastAPI
from core.config import setup_cors
from routers import story



app = FastAPI()
setup_cors(app)

app.include_router(story.router)

@app.get("/")
def health_check():
    return {"status": "ok"}
