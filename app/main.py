#importing necessary libraries
from fastapi import FastAPI, UploadFile, File
import pdfplumber
import docx
from app.processor import extract_text
from models.checker import check_visa_eligibility

app = FastAPI()

# accept file - uploading a pdf and matching with criteria
@app.post("/assess")
async def assess_cv(file: UploadFile = File(...)):
    text = await extract_text(file)
    if not text:
        return {"error": "Sorry! Unable to extract text from the file"}

    result = check_visa_eligibility(text)
    return result

# to confirm if api is running
@app.get("/")
def root():
    return {"message": "Visa Assessment API is now running!"}

