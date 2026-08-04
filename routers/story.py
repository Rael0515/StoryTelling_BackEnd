from pydantic import BaseModel

class StroyRequest(BaseModel):
    keywords: list[str]


@app.post("/api/generate")
def generate_story(request: StroyRequest):
    return {"story": "'{','.join(request.keywords)}' 키워드로 만든 짧은 스토리 입니다."}
