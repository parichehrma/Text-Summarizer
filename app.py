# Import system and OS tools for running training script
# FastAPI → API creation
# Uvicorn → run server
# Jinja2 → UI templates (optional)
# Starlette → response handling

import sys
import os
from fastapi import FastAPI # Import FastAPI framework to create web API
import uvicorn # Import uvicorn to run the FastAPI app
from fastapi.templating import Jinja2Templates # Import template system (not used yet, for future UI pages)
from starlette.responses import RedirectResponse # Redirect user to another URL (used for root endpoint)
from fastapi.responses import Response # Return plain text/response messages
from textsummarizer.pipeline.prediction import PredictionPipeline # Import custom prediction pipeline (your trained model inference)


# Sample default text (for testing)
text: str = "What is Text Summarization?"

# Create and Initialize FastAPI app instance
app = FastAPI()
# Root endpoint of the API
# Redirects user to Swagger UI documentation page
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs") # This redirects the user to the FastAPI automatic documentation UI (Swagger UI).
# /docs → Swagger UI (interactive API testing page)
# /redoc → alternative documentation UI


# Endpoint to trigger model training process
@app.get("/train")
async def training():
    try:
        os.system("python main.py") # Runs main.py file which starts full training pipeline       
        return Response("Training successful !!")  # Returns success message after training completes

    except Exception as e:
        return Response(f"Error Occurred! {e}")    # Returns error message if training fails

# Endpoint for prediction (text summarization)
# Takes user input text and returns generated summary
@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()        # Create prediction pipeline object (loads trained model)
        text = obj.predict(text)         # Generate summary from input text using model
        return text         # Return generated summary to user


    except Exception as e:         # Raise error if prediction fails
        raise e


# Entry point to run FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)     # Start server on host 127.0.0.1 and port 8080
