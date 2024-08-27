from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import uvicorn

# Load the model
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the FastAPI app
app = FastAPI()

# Define request and response models
class TextData(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str

# Define the sentiment analysis endpoint
@app.post("/analyze_sentiment", response_model=SentimentResponse)
def analyze_sentiment(data: TextData):
    try:
        prediction = model.predict([data.text])[0]
        return SentimentResponse(sentiment=prediction)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
