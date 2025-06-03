from fastapi import APIRouter
from fastapi.responses import FileResponse
from models.sensor_data import SensorData
from services.report_generator import generate_pdf_report
from services.genai_summary import generate_genai_summary
import numpy as np
import joblib

router = APIRouter()

# Lets load the models and scalers once at startup
reg_model = joblib.load("risk_score_model.joblib")
clf_model = joblib.load("issue_classifier.joblib")
scaler = joblib.load("scaler.joblib")
label_encoder = joblib.load("label_encoder.joblib")

@router.post("/predict")
def predict(data: SensorData):
    X = np.array([[data.pressure, data.flow_rate, data.temperature, data.vibration]])
    X_scaled = scaler.transform(X)

    risk_score = float(reg_model.predict(X_scaled)[0])
    issue_encoded = clf_model.predict(X_scaled)[0]
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
    filepath, filename = generate_pdf_report(data)
    return FileResponse(filepath, media_type='application/pdf', filename=filename)

@router.post("/generate-summary")
def generate_summary(data: SensorData):
    X = np.array([[data.pressure, data.flow_rate, data.temperature, data.vibration]])
    X_scaled = scaler.transform(X)

    risk_score = float(reg_model.predict(X_scaled)[0])
    issue_encoded = clf_model.predict(X_scaled)[0]
    issue_label = label_encoder.inverse_transform([issue_encoded])[0]
    severity = "High" if risk_score > 75 else "Medium" if risk_score > 50 else "Low"
    summary = generate_genai_summary(data, risk_score, issue_label, severity)


    
    return {
        "summary": summary,
        "risk_score": round(risk_score, 2),
        "issue": issue_label,
        "severity": severity,
    }

