import os 
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_genai_summary(data, risk_score, issue, severity):
    if not GROQ_API_KEY:
        return "Groq API key is missing. Cannot generate GenAI summary"
    
    prompt = (
        f"You are a pipeline integrity specialist.\n\n"
        f"Sensor Readings:\n"
        f"- Pressure: {data.pressure} psi\n"
        f"- Flow Rate: {data.flow_rate} m³/s\n"
        f"- Temperature: {data.temperature} °C\n"
        f"- Vibration: {data.vibration} g\n"
        f"- Risk Score: {risk_score:.2f}\n"
        f"- Issue: {issue}\n"
        f"- Severity: {severity}\n\n"
        f"Based on this data, write a short professional report (2–3 sentences) summarizing the situation and suggesting a course of action."
    )
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Debugging by printing the response
        print("GenAI Response:", data)
        
        
        return data['choices'][0]['message']['content']
    except Exception as e:
        print("Groq GenAI API error:", str(e))
        return f"GenAI failed to generate summary: {str(e)}"
