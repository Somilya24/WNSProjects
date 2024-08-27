# Sentiment Analysis API

## Project Background

This project implements a sentiment analysis model using the Naive Bayes algorithm and serves the model through a FastAPI web service. The model is trained on the NLTK movie reviews dataset and can predict whether a given text is positive or negative in sentiment. The project demonstrates how to build, train, and deploy a sentiment analysis model, making it accessible through a REST API.

## How to Run the Code

### Prerequisites

- Python 3.x
- FastAPI
- Uvicorn
- scikit-learn
- NLTK
- pandas

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Somilya24/WNSProjects.git
   cd Sentiment_Analysis_Api
2. **Install Required Python Packages**

    Make sure you have pip installed. Then, install the necessary packages:
    
    ```bash
      pip install -r requirements.txt
     ```
    If you don't have a requirements.txt file, manually install the required packages:
    
    ```bash
      pip install nltk scikit-learn fastapi uvicorn
    ```
3. **Download NLTK Data**

The script requires the movie_reviews dataset from NLTK. Run the following command to download it:

   ```python
    python -c "import nltk; nltk.download('movie_reviews')"
   ```
4. **Train the Sentiment Analysis Model**

Run the SentimentAnalysisModel.py script to train the model and save it as a pickle file:

   ```bash
   python SentimentAnalysisModel.py
   ```
After running this script, a file named sentiment_model.pkl will be created in your project directory.

5. **Run the FastAPI Application**

Start the FastAPI application by running the SentimentAnalysisApi.py script:

   ```bash
   python SentimentAnalysisApi.py
   ```
This will start the server on http://0.0.0.0:8000/.

6. **Test the API**

You can test the API using tools like curl or Postman. For example, using curl:

   ```bash
   curl -X POST "http://127.0.0.1:8000/analyze_sentiment" -H "Content-Type: application/json" -d '{"text": "I did not like the movie."}'
   ```

## Post-Run Example Screenshots
Below are some example screenshots of the application in action, along with commentary:

1. Model Training Output

Description: The console output after running SentimentAnalysis.py, showing the model’s accuracy on the test data.

![Screenshot (531)](https://github.com/user-attachments/assets/a6e86093-839e-4bae-93ab-8d4f70dc9d95)

2. API Request and Response

Description: A screenshot showing a sample request to the /analyze_sentiment endpoint and the response received, indicating the sentiment prediction.

![Screenshot (532)](https://github.com/user-attachments/assets/ad4779f7-7011-4592-92d5-5966c5003cd7)

## Conclusion
This project demonstrates the process of training a sentiment analysis model and deploying it as a REST API using FastAPI. The API can be further extended or integrated into larger applications requiring sentiment analysis capabilities.
