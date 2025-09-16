// Function to print all pages in order
function printAllPages() {
    // Show loading indicator
    const printButton = document.getElementById('printButton');
    const originalText = printButton.textContent;
    printButton.textContent = 'Generating PDF...';
    printButton.disabled = true;
    
    // Call the server endpoint to generate and download the PDF
    fetch('/api/print')
        .then(response => {
            if (response.ok) {
                return response.blob();
            } else {
                throw new Error('Failed to generate PDF');
            }
        })
        .then(blob => {
            // Create download link
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'openaxiom_manual.pdf';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
            
            // Restore button
            printButton.textContent = originalText;
            printButton.disabled = false;
        })
        .catch(error => {
            console.error('Error generating PDF:', error);
            alert('Error generating PDF. Please try again.');
            // Restore button
            printButton.textContent = originalText;
            printButton.disabled = false;
        });
}