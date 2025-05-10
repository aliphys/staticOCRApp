# Azure Static Web App for PDF Data Extraction

This project demonstrates a basic structure for a static web application hosted on Azure that allows users to upload a PDF file and extract data using an Azure Function backend.

**Frontend:**
- Built with basic HTML, CSS, and JavaScript.
- Allows users to select and upload PDF files.
- Sends the PDF to the backend Azure Function for processing.
- Displays the extracted data received from the backend.

**Backend (Azure Function):**
- A Python Azure Function that receives the uploaded PDF.
- **Currently contains a placeholder for PDF processing logic.** 
- Returns the extracted data as a JSON response.

**Next Steps:**
- Set up your Azure Static Web App resource in the Azure portal.
- Configure the API endpoint to link to your Azure Function.
- Implement the PDF data extraction logic in the `api/function.py` file using Azure Document Intelligence or a suitable library.
- Deploy the frontend files to your Azure Static Web App.
- Deploy the Azure Function code.