from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from Schema.user_input import Input

import pickle
from Model.model import model, predict_output


app = FastAPI()


## Human Readable
@app.get('/')
def home():
    return {'message': 'Premium Insuramce Prediction API'}

## Matchine Readable
@app.get('/health')
def health_check():
    return {
       'status': 'OK' 
    }
        
@app.post("/predict")
def predict(data: Input):
    input_df ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
     }
    try:

        prediction = predict_output(input_df)
        return JSONResponse(status_code = 200, content={"Result": prediction})
    except Exception as e:
        return JSONResponse(status_code = 500, content = str(e))
    