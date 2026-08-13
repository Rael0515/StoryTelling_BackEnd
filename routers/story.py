from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()



class StoryRequest(BaseModel):
    keywords: list[str]
@router.post("/api/generate")
def generate_story(request: StoryRequest):
    return {"story": f"'{','.join(request.keywords)}' 키워드로 만든 짧은 스토리 입니다."}
