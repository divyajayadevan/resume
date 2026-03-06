import PyPDF2
import docx
import io

def extract_text(file) -> str:
    filename = file.name.lower()
    text = ""
    
    if filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
                
    elif filename.endswith('.docx'):
        doc = docx.Document(io.BytesIO(file.read()))
        for para in doc.paragraphs:
            text += para.text + "\n"
            
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
        
    return text.strip()