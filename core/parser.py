from pypdf import PdfReader
import io

def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extracts raw text content from an uploaded PDF file object safely.
    """
    try:
        pdf_stream = io.BytesIO(uploaded_file.read())
        reader = PdfReader(pdf_stream)
        
        extracted_text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"
                
        return extracted_text.strip()
    except Exception as e:
        raise RuntimeError(f"Error executing PDF text extraction pipeline: {str(e)}")