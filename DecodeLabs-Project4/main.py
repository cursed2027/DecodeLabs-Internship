# DecodeLabs AI Internship
# Project 4 - OCR Text Recognition
# Name: Chottu Mukati

import os
import cv2
import pytesseract

# Path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Get the current project directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the image
image_path = os.path.join(current_dir, "images", "receipt.png")

# Load image
image = cv2.imread(image_path)

# Check whether image is loaded successfully
if image is None:
    print("Error: Image not found.")
    print("Expected location:", image_path)
    exit()

print("Image Loaded Successfully!")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Remove noise using Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding for better OCR accuracy
processed = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)[1]

# Extract text using OCR
text = pytesseract.image_to_string(processed)

# Display extracted text
print("\n========== Extracted Text ==========\n")

if text.strip():
    print(text)
else:
    print("No readable text detected.")

print("\n====================================")