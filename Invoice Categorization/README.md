# Invoice Tagging and Categorization
## Project Background
The goal of this project is to automate the categorization of invoice descriptions into predefined categories. The project utilizes a BERT-based model trained on synthetic data to classify invoice descriptions into categories such as "Office Supplies," "Marketing and Advertising," "Utilities," etc. The process involves extracting text from PDF invoices using OCR (Optical Character Recognition) and then categorizing the text using the trained model.

This solution is valuable for businesses looking to automate the processing of invoices, reducing manual effort, and improving accuracy in categorizing expenses.

## Project Structure
- **train_model_invoice.py:** Script for training the BERT model on invoice descriptions.
- **InvoiceTagging.py:** Main application script that uses the trained model to categorize text extracted from PDF invoices.
- **InputFiles/:** Directory containing sample PDF invoices for testing.
- **model/:** Directory where the trained model and tokenizer are saved.
## Prerequisites
- Python 3.8 or higher
- Install required Python libraries:
  ```bash
    pip install torch transformers spacy pytesseract pdf2image
- Install Tesseract OCR:
  - Windows: Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
  - Linux: Install via package manager (`sudo apt-get install tesseract-ocr`).
  - macOS: Install via Homebrew (`brew install tesseract`).
## How to Run the Code
1. **Train the Model:** If you haven't trained the model yet, run the `train_model_invoice.py` script to train the BERT model on the synthetic invoice descriptions.

    ```bash
    python train_model_invoice.py

This script will generate synthetic training data, train the BERT model on this data, and save the model in the `model/` directory.

2. **Categorize Invoices:** Once the model is trained, you can use the `InvoiceTagging.py` script to categorize invoices. This script takes PDF files as input, extracts the text using OCR, and categorizes the invoice descriptions.
    ```bash
    python InvoiceTagging.py --pdf_folder InputFiles/
This command will process all PDF files in the `InputFiles/` directory and print the category for each invoice description.

## Example Run and Screenshots

1. Categorizing Invoices

- The text is extracted from a sample PDF invoice using Tesseract OCR.
- The extracted text is then passed through the trained BERT model.
- The output is the predicted category for the invoice.

![Screenshot (524)](https://github.com/user-attachments/assets/8f9f8a57-20e3-42b9-9a77-36e06c02729c)


## Important Notes
- The `train_model_invoice.py` script uses synthetic data for training.For production use, you would train the model on real invoice data.
- OCR accuracy depends on the quality of the scanned invoices.
- The categories used in this project are based on typical business expenses. You can modify the categories as per your needs.
