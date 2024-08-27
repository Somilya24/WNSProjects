# Invoice Processing with Bounding Boxes

## Project Background

This project is a Streamlit-based application that processes invoices (in PDF format) to extract text and highlight relevant information such as dates, amounts, and keywords like "total", "invoice", "amount", and "date" with bounding boxes. The application uses Tesseract OCR for text extraction and OpenCV for image processing.

### Features
- **PDF Text Extraction:** Extracts text from uploaded PDF files using OCR (Optical Character Recognition).
- **Keyword Highlighting:** Identifies and highlights key information in the invoice with bounding boxes.
- **User-Friendly Interface:** Provides a simple interface for uploading invoices and viewing processed images.

## How to Run the Code

### Prerequisites
- Python 3.x
- Tesseract-OCR installed (Ensure `pytesseract.pytesseract.tesseract_cmd` is set to the correct path)

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/invoice-processing-bounding-boxes.git
   cd invoice-processing-bounding-boxes

2. **Install Required Packages:**
Install the required Python libraries using pip:

    ```bash
    pip install streamlit opencv-python pytesseract pdf2image python-docx numpy
3. **Run the Application:**
Execute the script using Streamlit:

   ```bash
   streamlit run main.py
## Usage
1. **Upload an Invoice:**

   Click the "Browse files" button to upload a PDF invoice.


2. **View Processed Invoice:** 

   The application will extract the text and display the invoice image with bounding boxes around identified keywords and dates.

## Example Screenshots
1. Application Interface:
This screenshot shows the main interface of the application, where the user can upload a PDF invoice.

![Screenshot (520)](https://github.com/user-attachments/assets/7bfe4792-d8ab-4679-9819-051283442156)
3. Processed Invoice:
This screenshot shows a processed invoice with bounding boxes highlighting dates, amounts, and other relevant keywords.

![Screenshot (521)](https://github.com/user-attachments/assets/3fdce171-be3c-44ac-9210-c6631a0c5e15)

## Important Notes
- **Tesseract Installation:** Ensure that Tesseract is correctly installed and its path is correctly set in the code (pytesseract.pytesseract.tesseract_cmd).
- **File Support:** Currently, the application only supports PDF files.

## Conclusion
   This application provides a convenient way to process invoices, extract important information, and visualize it with bounding boxes. It's an ideal tool for anyone looking to automate invoice processing or enhance document analysis.
