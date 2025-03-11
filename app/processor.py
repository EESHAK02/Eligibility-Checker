# importing necessary libraries
import pdfplumber
import docx
from typing import Optional
import pytesseract
from pdf2image import convert_from_path
from PIL import Image, ImageFilter
import numpy as np
import cv2

# setting path for tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# can detect text from pdf,docx, or image file file, else gives error
async def extract_text(file):
    try:
        if file.filename.endswith(".pdf"):
            with pdfplumber.open(file.file) as pdf:
                text = "\n".join([page.extract_text(layout=True) or '' for page in pdf.pages])
                if text.strip():  
                    return text.strip()
        
        elif file.filename.endswith(".docx"):
            doc = docx.Document(file.file)
            return "\n".join([para.text for para in doc.paragraphs]).strip()

        elif file.filename.endswith((".jpg", ".jpeg", ".png")):
        
            img = Image.open(file.file)

            #print(f"Image loaded: {img.format}, {img.size}, {img.mode}")

            text = pytesseract.image_to_string(img)
            #print("OCR result:", text)

            if not text.strip():
                raise ValueError("OCR failed.")

            return text.strip()

        else:
            return None
        
    except Exception as e:
        print(f"Error in text extraction: {e}")
        return None
