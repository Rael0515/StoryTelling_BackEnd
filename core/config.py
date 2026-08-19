from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    app.add_middleware( #미들웨어는 모든 app가 거치는 함수
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # 나중에 Vercel 도메인 추가
        allow_methods=["*"],
        allow_headers=["*"],
    )



## 임시 파일
