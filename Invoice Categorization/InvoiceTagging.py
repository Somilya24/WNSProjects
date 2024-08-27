# main_app.py
import pytesseract
from pdf2image import convert_from_path
import spacy
from transformers import BertTokenizer, BertForSequenceClassification
from PIL import Image
import torch
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the categories
category_names = {
    0: "Office Supplies",
    1: "Marketing and Advertising",
    2: "Utilities",
    3: "Software Licenses",
    4: "Professional Services",
    5: "Rent",
    6: "Travel and Accommodation",
    7: "Meals and Entertainment",
    8: "Maintenance and Repairs",
    9: "Transportation",
    10: "Insurance",
    11: "Salaries and Wages",
    12: "Training and Development",
    13: "Telecommunications",
    14: "Health and Safety",
    15: "Taxes and Compliance",
    16: "Inventory and Stock",
    17: "Loan Repayment",
    18: "Technology and IT Services",
    19: "Employee Benefits",
    20: "Sales",
    21: "Groceries"
}

# Load the model and tokenizer
def load_model(model_dir='model'):
    model = BertForSequenceClassification.from_pretrained(model_dir)
    tokenizer = BertTokenizer.from_pretrained(model_dir)
    return model, tokenizer

# Extract text from PDF invoices using OCR
# Step 1: Extract text from PDF invoices using OCR
def extract_text_from_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in [".pdf"]:
        pages = convert_from_path(file_path)
        invoice_text = ""
        for page in pages:
            invoice_text += pytesseract.image_to_string(page)
        return invoice_text

    elif file_extension in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)

    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

# Preprocess the text using spaCy
def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# Categorize the invoice and display category name
def categorize_invoice(model, tokenizer, text, category_names):
    encoding = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    output = model(**encoding)
    predicted_label = output.logits.argmax(dim=1).item()
    return category_names[predicted_label]

# Tag the invoice with relevant entities using NER
def tag_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Main function to process an invoice
def process_invoice(pdf_path, model, tokenizer, category_names):
    # Extract text
    invoice_text = extract_text_from_file(pdf_path)
    print(f"Extracted Text: {invoice_text}\n")

    # Preprocess text
    preprocessed_text = preprocess_text(invoice_text)

    # Categorize invoice and get category name
    category = categorize_invoice(model, tokenizer, preprocessed_text, category_names)
    print(f"Invoice Category: {category}\n")

# Example usage
if __name__ == "__main__":
    # Load the trained model and tokenizer
    model, tokenizer = load_model()

    # Process a new invoice
    process_invoice('InputFiles/medical-store-cash-memo.jpg', model, tokenizer, category_names)
