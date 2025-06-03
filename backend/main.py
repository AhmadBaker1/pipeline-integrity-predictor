from fastapi import FastAPI
from routes.report_routes import router as report_router
from routes.predictor import router as predictor_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "Backend is running!"}

app.include_router(report_router)
app.include_router(predictor_router)
