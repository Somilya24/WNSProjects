import streamlit as st
import cv2
import pytesseract
from pdf2image import convert_from_path
import numpy as np
import tempfile
import os
import re

# Update this path if Tesseract is installed in a different location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define colors
key_field_color = (0, 0, 255)  # Blue for key fields
numerical_color = (0, 255, 0)  # Green for numerical values
table_color = (255, 0, 0)  # Red for tables

def extract_text_from_pdf(file_path):
    try:
        images = convert_from_path(file_path)
        all_text = []
        for image in images:
            text = pytesseract.image_to_string(np.array(image), config='--psm 6')
            all_text.append(text)
        return all_text, [np.array(img) for img in images]
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return None, None

def draw_bounding_boxes(img, text):
    try:
        h, w, _ = img.shape
        boxes = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        n_boxes = len(boxes['text'])

        for i in range(n_boxes):
            if int(boxes['conf'][i]) > 0:  # Only consider confident detections
                x, y, bw, bh = boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i]
                text_value = boxes['text'][i].lower()

                # Determine color based on content
                if re.search(r'\b(total|invoice|amount|date|order|no)\b', text_value):
                    color = key_field_color
                elif re.search(r'\d+(\.\d+)?', text_value):
                    color = numerical_color
                elif re.search(r'\btable\b', text_value):  # Assuming the presence of "table" in the text indicates a table
                    color = table_color
                else:
                    color = table_color

                # Draw the rectangle
                img = cv2.rectangle(img, (x, y), (x + bw, y + bh), color, 2)
        return img
    except Exception as e:
        st.error(f"Error drawing bounding boxes: {e}")
        return img

def process_file(uploaded_file):
    try:
        _, ext = os.path.splitext(uploaded_file.name)
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        if ext.lower() == '.pdf':
            all_texts, images = extract_text_from_pdf(file_path)

            if images is not None:
                processed_images = []
                for img, text in zip(images, all_texts):
                    img_with_boxes = draw_bounding_boxes(img, text)
                    processed_images.append(img_with_boxes)
                return processed_images

        else:
            st.error("Unsupported file format")
            return None

    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None

st.title("Invoice Processing with Bounding Boxes")

uploaded_file = st.file_uploader("Upload an invoice (PDF)", type=['pdf'])

if uploaded_file is not None:
    processed_images = process_file(uploaded_file)
    if processed_images is not None:
        for i, img in enumerate(processed_images):
            st.image(img, caption=f'Processed Invoice - Page {i + 1}', use_column_width=True)
