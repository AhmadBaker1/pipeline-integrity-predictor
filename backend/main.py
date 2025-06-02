from fastapi import FastAPI
from routes.report_routes import router

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "Backend is running!"}

app.include_router(router)
