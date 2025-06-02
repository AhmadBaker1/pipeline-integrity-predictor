from pydantic import BaseModel

'''
 I will add a /predict endpoint which will accept sensor data and return a
 simulated integrity score.
'''
class SensorData(BaseModel):
    pressure: float
    flow_rate: float
    temperature: float
    vibration: float