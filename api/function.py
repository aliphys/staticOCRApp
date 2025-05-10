import logging
import azure.functions as func
import json
# from azure.ai.formrecognizer import DocumentAnalysisClient
# from azure.core.credentials import AzureKeyCredential

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        file = req.files.get('pdfFile')
        if file:
            file_bytes = file.stream.read()
            logging.info(f"File size received: {len(file_bytes)} bytes")

            # --- Placeholder for your PDF processing logic ---
            extracted_data = {
                "filename": file.filename,
                "size": len(file_bytes),
                "data": "This is where the extracted data would go..."
            }
            # --- End of placeholder ---

            return func.HttpResponse(
                json.dumps(extracted_data),
                mimetype="application/json"
            )
        else:
            return func.HttpResponse(
                 "Please upload a PDF file.",
                 status_code=400
            )
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return func.HttpResponse(
             f"Error processing request: {e}",
             status_code=500
        )

if __name__ == "__main__":
    # This is for local testing
    class MockHttpRequest:
        def __init__(self, files=None):
            self.files = files or {}

    class MockFile:
        def __init__(self, filename, content):
            self.filename = filename
            self.content = content

        def stream(self):
            return self

        def read(self):
            return self.content

    # Example local test
    with open("dummy.pdf", "rb") as f:
        mock_pdf = f.read()

    mock_req = MockHttpRequest(files={'pdfFile': MockFile(filename="test.pdf", content=mock_pdf)})
    response = main(mock_req)
    if response:
        print(f"Status Code: {response.status_code}")
        print(f"Body: {response.get_body()}")