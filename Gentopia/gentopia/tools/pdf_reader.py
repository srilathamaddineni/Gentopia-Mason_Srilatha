from typing import AnyStr
from gentopia.tools.basetool import BaseTool, BaseModel, Field
from PyPDF2 import PdfReader

class ReadPdfArgs(BaseModel):
    file_path: str = Field(..., description="path to the PDF file")

class ReadPdf(BaseTool):
    """Tool that reads text content from a PDF file."""

    name = "read_pdf"
    description = "A tool to extract text content from a PDF file."

    args_schema: Optional[Type[BaseModel]] = ReadPdfArgs

    def _run(self, file_path: AnyStr) -> str:
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)
            text = ''
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    pdf_path = 'Srilatha_Maddineni_HW3'
    ans = ReadPdf()._run(pdf_path)
    print(ans)
