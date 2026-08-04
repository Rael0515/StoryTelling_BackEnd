from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 나중에 Vercel 도메인 추가
    allow_methods=["*"],
    allow_headers=["*"],
)