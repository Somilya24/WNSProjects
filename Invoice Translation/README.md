# Invoice Translation and Language Detection
## Project Background
This project is designed to process invoices in various formats (PDF, images, text files) and detect the language of the content using NLP tools. It then translates the content into English using a pre-trained machine translation model. The translated content is saved as separate text files for each invoice. The project leverages spaCy for language detection, pytesseract for text extraction from images, and transformers for translation.

## Requirements
Before running the project, ensure you have installed the following libraries:

- Python 3.7+
- pandas
- pytesseract
- pdf2image
- spacy
- transformers

You also need to have Tesseract OCR installed on your machine. You can download it from here.

## Setup Instructions
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Somilya24/WNSProjects.git
2. Navigate to the project directory:
   ```bash
    cd Invoice Translation
3. Install the required Python libraries:
   ```bash
    pip install -r requirements.txt
4. Ensure that Tesseract OCR is installed and update the `pytesseract.pytesseract.tesseract_cmd` path in the code to point to your Tesseract executable.
## Running the Code
1. Place your invoice files (PDFs, images, or text files) in the `InputFiles` directory.
2. Run the script:
   ```bash
    python InvoiceTranslator.py
3. The translated invoices will be saved in the `translated_invoices` directory.

## Example Run and Output
When you run the script, it processes each invoice file, detects the language, translates the content to English, and saves the translated text in a new file. Here’s a sample output:

   ```bash
   Translated invoice saved to: C:\Your\anand\PycharmProjects\Task2\translated_invoices\invoice1_translated.txt
   Translated invoice saved to: C:\Users\anand\PycharmProjects\Task2\translated_invoices\invoice2_translated.txt
   ...
   Translation complete. Translated invoices saved to: C:\Users\anand\PycharmProjects\Task2\translated_invoices
```
## Screenshot of Application Running
![Screenshot (525)](https://github.com/user-attachments/assets/3a60b2d2-e580-49e3-a2cf-f8f6658c5da8)
The above screenshot shows the script processing invoices and saving translated versions in the specified directory.

## Issues and Error Handling
The script includes basic error handling for issues such as file reading errors, language detection, and translation errors. If any errors occur during processing, the script will print an error message to the console and continue with the next file.
