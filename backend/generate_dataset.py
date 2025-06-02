import pandas as pd
import numpy as np
import random

def generate_data(n=1000):
    data = []

    for _ in range(n):
        pressure = round(np.random.uniform(100, 160), 2)
        flow_rate = round(np.random.uniform(10, 20), 2)
        temperature = round(np.random.uniform(20, 45), 2)
        vibration = round(np.random.uniform(0.001, 0.15), 4)

        # The risk logic here will be high pressure + high vibration = high risk
        score = (
            0.4 * (pressure - 100) +
            0.3 * (flow_rate - 10) +
            0.2 * (temperature - 20) +
            100 * vibration 
        )
        risk_score = min(max(round(score + np.random.normal(0, 5), 2), 0), 100)

        ## Issue type logic 
        if pressure > 150 and vibration > 0.1:
            issue_type = "Fatigue"
        elif pressure > 140 and temperature > 40:
            issue_type = "Corrosion"
        elif flow_rate < 18 and temperature < 30:
            issue_type = "Leakage"
        else:
            issue_type = "None"

        data.append([
            pressure, flow_rate, temperature, vibration, risk_score, issue_type
        ])

    df = pd.DataFrame(data, columns=[
        "pressure", "flow_rate", "temperature", "vibration", "risk_score", "issue_type"
    ])
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("pipeline_data.csv", index=False)
    print("Dataset generated and saved to pipeline_data.csv")