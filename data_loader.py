from pathlib import Path
from llama_index.core import SimpleDirectoryReader, Document
from PyPDF2 import PdfReader
from typing import List, Dict

def load_resumes(data_dir: Path) -> List[Document]:
    """Load resumes as LlamaIndex Document objects with metadata"""
    documents = []
    
    for pdf_file in data_dir.glob("*.pdf"):
        with open(pdf_file, "rb") as f:
            pdf_reader = PdfReader(f)
            text = "\n".join([page.extract_text() for page in pdf_reader.pages])
            
            # Create Document with proper structure
            documents.append(
                Document(
                    text=text,
                    metadata={
                        "file_name": pdf_file.name,
                        "pages": len(pdf_reader.pages)
                    }
                )
            )
    
    return documents 