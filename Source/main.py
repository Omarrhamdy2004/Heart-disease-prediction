from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
try:
    model = joblib.load("project.pkl")
except Exception as e:
    print(f"Error loading model: {e}")
    raise
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float
    feature6: float
    feature7: float
    feature8: float
    feature9: float
    feature10: float
    feature11: float

@app.get("/")
def home(): 
    return {"message": "API is running ✅"}

@app.post("/predict")
def predict(data: InputData):
    features = [[
        data.feature1,
        data.feature2,
        data.feature3,
        data.feature4,
        data.feature5,
        data.feature6,
        data.feature7,
        data.feature8,
        data.feature9,
        data.feature10,
        data.feature11
    ]]
    
    try:
        prediction = model.predict(features)
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

    return {"prediction": int(prediction[0])}