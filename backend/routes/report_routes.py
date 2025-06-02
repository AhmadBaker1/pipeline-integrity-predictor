from fastapi import APIRouter
from fastapi.responses import FileResponse
from models.sensor_data import SensorData
from services.report_generator import generate_pdf_report
import random

router = APIRouter()

@router.post("/predict",)
def predict(data: SensorData):

    # Simulating a fake risk score that is between 0 and 100
    risk_score = round(random.uniform(20, 95), 2) # generate fake risk score between 20 and 95 limit to 2 d.p

    issues = ["Corrosion Risk", "Fatigue Risk", "Leakage Risk", "Overpressure Risk"]
    detected_issue = random.choice(issues)

    severity = "High" if risk_score > 75 else "Medium" if risk_score > 50 else "Low"
    full_issue = f"{detected_issue} - {severity}"

    return {
        "risk_score": risk_score,
        "detected_issue": f"{detected_issue} - {severity}",
        "input": data.dict()
    }

@router.post("/generate-report")
def generate_report(data: SensorData):
    file_path, file_name = generate_pdf_report(data)
    return FileResponse(file_path, media_type='application/pdf', filename=file_name)