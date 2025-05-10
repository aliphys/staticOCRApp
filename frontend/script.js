async function uploadPdf() {
    const fileInput = document.getElementById('pdfFile');
    const outputDiv = document.getElementById('output');
    const file = fileInput.files[0];

    if (!file) {
        outputDiv.innerText = 'Please select a PDF file.';
        return;
    }

    const formData = new FormData();
    formData.append('pdfFile', file);

    try {
        const response = await fetch('/api/extract', { // Assuming your Azure Function endpoint is /api/extract
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            outputDiv.innerText = JSON.stringify(data, null, 2); // Display extracted data
        } else {
            const error = await response.text();
            outputDiv.innerText = `Error: ${response.status} - ${error}`;
        }
    } catch (error) {
        outputDiv.innerText = `Error: ${error.message}`;
    }
}