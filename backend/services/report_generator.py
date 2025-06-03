from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from services.genai_summary import generate_genai_summary
import joblib
import numpy as np
import os
import uuid
from models.sensor_data import SensorData
import random
import textwrap


# Load the trained models and scaler
reg_model = joblib.load("risk_score_model.joblib")
clf_model = joblib.load("issue_classifier.joblib")
scaler = joblib.load("scaler.joblib")
label_encoder = joblib.load("label_encoder.joblib")


def generate_pdf_report(data: SensorData):
    X = np.array([[data.pressure, data.flow_rate, data.temperature, data.vibration]])
    X_scaled = scaler.transform(X)

    # Predicting the risk score (regression model)
    risk_score = float(reg_model.predict(X_scaled)[0])

    # Predicting the issue (classification model)
    issue_encoded = clf_model.predict(X_scaled)[0]
    issue_label = label_encoder.inverse_transform([issue_encoded])[0]

    # Now determine the severity of the issue
    severity = "High" if risk_score > 75 else "Medium" if risk_score > 50 else "Low"
    full_issue = f"{issue_label} - {severity}"

    # Generate a summary using GenAI
    summary = generate_genai_summary(data, risk_score, issue_label, severity)

    filename = f"report_{uuid.uuid4().hex[:8]}.pdf"
    filepath = os.path.join("reports", filename)

    c = canvas.Canvas(filepath, pagesize=letter)
    text = c.beginText(50, 750)
    text.setFont("Helvetica", 12)

    text.textLine("Pipeline Integrity Risk Report")
    text.textLine("------------------------------------")
    text.textLine(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    text.textLine(f"Pressure: {data.pressure} psi")
    text.textLine(f"Flow Rate: {data.flow_rate} m³/s")
    text.textLine(f"Temperature: {data.temperature} °C")
    text.textLine(f"Vibration: {data.vibration} g")
    text.textLine(f"Risk Score: {risk_score}")
    text.textLine(f"Detected Issue: {full_issue}")
    text.textLine("")

    text.textLine("Summary:")
    # Wrap the summary text to fit within the PDF width
    wrapped_lines = textwrap.wrap(summary, width=95)
    for line in wrapped_lines:
        text.textLine(line)

    text.textLine("Please review maintenance suggestions based on severity.")

    c.drawText(text)
    c.showPage()
    c.save()

    return filepath, filename