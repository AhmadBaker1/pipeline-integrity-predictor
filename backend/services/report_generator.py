from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import uuid
from models.sensor_data import SensorData
import random

def generate_pdf_report(data: SensorData):
    risk_score = round(random.uniform(20, 95), 2)
    issues = ["Corrosion Risk", "Fatigue Risk", "Leak Risk", "Overpressure Risk"]
    detected_issue = random.choice(issues)
    severity = "High" if risk_score > 75 else "Medium" if risk_score > 50 else "Low"
    full_issue = f"{detected_issue} – {severity}"

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
    text.textLine("Summary: Pipeline integrity is at risk. Recommended inspection required.")
    text.textLine("Please review maintenance suggestions based on severity.")

    c.drawText(text)
    c.showPage()
    c.save()

    return filepath, filename