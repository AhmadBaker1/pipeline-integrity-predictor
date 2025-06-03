from fastapi import APIRouter
from fastapi.responses import FileResponse
from models.sensor_data import SensorData
import numpy as np
from services.report_generator import generate_pdf_report, reg_model, clf_model, scaler, label_encoder
import random

router = APIRouter()

@router.post("/predict",)
def predict(data: SensorData):
    X = np.array([[data.pressure, data.flow_rate, data.temperature, data.vibration]])
    X_scaled = scaler.transform(X)

    risk_score = float(reg_model.predict(X_scaled)[0])
    issue_encoded = clf_model.predict(X_scaled)[0]
    print("Predicted encoded label:", issue_encoded)
    print("Available label classes:", label_encoder.classes_)
    issue_label = label_encoder.inverse_transform([issue_encoded])[0]
    severity = "High" if risk_score > 75 else "Medium" if risk_score > 50 else "Low"
    full_issue = f"{issue_label} - {severity}"

    return {
        "risk_score": round(risk_score, 2),
        "detected_issue": full_issue,
        "input": data.dict()
    }

@router.post("/generate-report")
def generate_report(data: SensorData):
    file_path, file_name = generate_pdf_report(data)
    return FileResponse(file_path, media_type='application/pdf', filename=file_name)